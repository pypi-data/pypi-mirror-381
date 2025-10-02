import inspect
import json
import logging
import re
from deepdiff import DeepDiff
from pathlib import Path
from typing import Any, TypeVar

import allure
import urllib3
from json_checker import Checker, CheckerError
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver

from promium.common import upload_screenshot


CoerceDict = dict[str, type] | None

log = logging.getLogger(__name__)

http = urllib3.PoolManager(
    cert_reqs=False,
    timeout=5,
    headers={
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
    },
)


def base_msg(msg: str) -> str:
    """Return message with trailing newline if provided."""
    return f"{msg}\n" if msg else ""


T = TypeVar("T")


def _check_namedtuple[T](obj: T) -> dict[str, Any] | T:
    """Convert namedtuple to dict if possible, otherwise return the object."""
    if hasattr(obj, "_asdict"):
        return obj._asdict()
    return obj


def convert_container(container: Any) -> dict | str:
    """Convert a container to a formatted JSON string, if not already
    a string."""
    if not isinstance(container, str):
        return json.dumps(
            obj=container,
            indent=4,
            sort_keys=True,
            ensure_ascii=False,
            default=str,
        )
    return _check_namedtuple(container)


def get_text_with_ignore_whitespace_symbols(text: str) -> str:
    """Return text with all whitespace symbols removed."""
    text_without_whitespace_symbols = (
        text.replace("\t", " ")
        .replace("\v", " ")
        .replace("\r", " ")
        .replace("\n", " ")
        .replace("\f", " ")
        .strip()
    )
    text_list = text_without_whitespace_symbols.split(" ")
    text_list_without_space = [word for word in text_list if word]
    return " ".join(text_list_without_space)


class PromiumAssertionError(AssertionError):
    """Immediate failure with Promium formatting."""


class BaseSoftAssertion:
    """Base class for soft assertion utilities."""

    assertion_errors: list[str] = []

    def _ensure_state(self) -> None:
        """Ensure instance fields exist when __init__ wasn't called."""
        if (
            not hasattr(self, "assertion_errors")
            or self.assertion_errors is None
        ):
            self.assertion_errors = []
        if not hasattr(self, "hard_assert"):
            self.hard_assert = False
        if not hasattr(self, "driver"):
            self.driver = None

    def _relpath(self, p: str) -> str:
        """Return relative path from current working directory."""
        try:
            return Path(p).resolve().relative_to(Path.cwd()).as_posix()
        except Exception:
            return Path(p).as_posix()

    def _callsite_line(self) -> str:
        """Return callsite line in format ↳ at path:lineno."""
        for frame in inspect.stack()[2:]:
            fn = frame.filename.replace("\\", "/")
            if "/site-packages/" in fn:
                continue
            return f"↳ at {self._relpath(fn)}:{frame.lineno}"
        f = inspect.stack()[2]
        return f"↳ at {self._relpath(f.filename)}:{f.lineno}"

    def _format_error(self, error_msg: str, *, with_screen: bool) -> str:
        """Build final error text."""
        screen = self.add_screenshot(error_msg) if with_screen else ""
        return f"{error_msg}{screen}\n{self._callsite_line()}\n"

    def _emit(
        self,
        error_msg: str,
        with_screen: bool,
        hard_assert_override: bool | None,
    ) -> None:
        self._ensure_state()
        formatted = self._format_error(error_msg, with_screen=with_screen)
        effective_hard_assert = (
            self.hard_assert
            if hard_assert_override is None
            else hard_assert_override
        )

        if effective_hard_assert:
            __tracebackhide__ = True
            title = "Hard Assertion Error"
            message = f"{title}\n\n{formatted}"
            raise AssertionError(message)

        self.assertion_errors.append(formatted)

    def add_screenshot(self, error_msg: str = "soft_assertion") -> str:
        """Attach screenshot to allure report if driver is available."""
        self._ensure_state()
        if getattr(self, "driver", None):
            try:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name=error_msg,
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                log.error(f"[PROMIUM] Can't attach screenshot: {e}")
            return f"\nScreenshot: {upload_screenshot(self.driver)}\n"
        return ""

    def soft_assert_true(
        self,
        expr: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that the expression is true."""
        if not expr:
            error = msg or "Is not true."
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )
            return error
        return None

    def soft_assert_false(
        self,
        expr: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that the expression is false."""
        if expr:
            error = msg or "Is not false."
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )
            return error
        return None

    def soft_assert_equals(
        self,
        current: Any,
        expected: Any,
        msg: str | None = None,
        *,
        show_diff: bool = False,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that current equals expected, optionally showing diff."""
        diff = None
        if type(current) is list and type(expected) is list:
            diff = DeepDiff(current, expected, ignore_order=True)
        if show_diff and type(current) is str and type(expected) is str:
            current_splitlines = current.splitlines()
            expected_splitlines = expected.splitlines()
            if len(current_splitlines) > 1 or len(expected_splitlines) > 1:
                diff = DeepDiff(current_splitlines, expected_splitlines)
        difference = f"\nDifference:\n{convert_container(diff)}" if diff else ""

        type_current = type_expected = ""
        if type(current) is not type(expected):
            type_current = f"({type(current)})"
            type_expected = f"({type(expected)})"

        assert_message = (
            f"{base_msg(msg)}\n"
            f"Current - {convert_container(current)} {type_current}\n"
            f"Expected - {convert_container(expected)} {type_expected}\n"
            f"{difference}"
        )
        return self.soft_assert_true(
            current == expected,
            assert_message,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_not_equals(
        self,
        current: Any,
        expected: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that current does not equal expected."""
        message = (
            f"{base_msg(msg)}\n"
            f"Current - {convert_container(current)}\n"
            f"Expected - {convert_container(expected)}\n"
        )
        return self.soft_assert_false(
            current == expected,
            message,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_in(
        self,
        member: Any,
        container: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that member is in container."""
        message = (
            f"{base_msg(msg)}\n"
            f"Member: '{member}'\n not found in\n"
            f"Container: '{convert_container(container)}'\n"
        )
        return self.soft_assert_true(
            member in container,
            message,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_not_in(
        self,
        member: Any,
        container: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that member is not in container."""
        message = (
            f"{base_msg(msg)}\n"
            f"Member: '{member}'\n unexpectedly found in\n"
            f"Container: '{convert_container(container)}'\n"
        )
        return self.soft_assert_true(
            member not in container,
            message,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_less_equal(
        self,
        a: Any,
        b: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that a is less than or equal to b."""
        error = f"{base_msg(msg)}{a} not less than or equal to {b}\n"
        return self.soft_assert_true(
            a <= b, error, with_screen=with_screen, hard_assert=hard_assert
        )

    def soft_assert_less(
        self,
        a: Any,
        b: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that a is less than b."""
        error = f"{base_msg(msg)}{a} not less than {b}\n"
        return self.soft_assert_true(
            a < b, error, with_screen=with_screen, hard_assert=hard_assert
        )

    def soft_assert_greater_equal(
        self,
        a: Any,
        b: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that a is greater than or equal to b."""
        error = f"{base_msg(msg)}{a} not greater than or equal to {b}\n"
        return self.soft_assert_true(
            a >= b, error, with_screen=with_screen, hard_assert=hard_assert
        )

    def soft_assert_greater(
        self,
        a: Any,
        b: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that a is greater than b."""
        error = f"{base_msg(msg)}{a} not greater than {b}\n"
        return self.soft_assert_true(
            a > b, error, with_screen=with_screen, hard_assert=hard_assert
        )

    def soft_assert_regexp_matches(
        self,
        text: str,
        expected_regexp: str,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Fail the test unless the text matches the regular expression."""
        pattern = re.compile(expected_regexp)
        result = pattern.search(text)
        if not result:
            error = (
                f"{base_msg(msg)}"
                f"Regexp didn't match."
                f"Pattern {str(pattern.pattern)} not found in {str(text)}\n"
            )
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )
            return error
        return None

    def soft_assert_disable(
        self,
        element: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that element has 'disabled' attribute."""
        default_msg = "" if msg else f"Not disabled {element}\n"
        error = f"{base_msg(msg)}{default_msg}"
        return self.soft_assert_true(
            element.get_attribute("disabled"),
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_is_none(
        self,
        obj: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that object is None."""
        default_msg = "" if msg else f"{obj} is not None.\n"
        error = f"{base_msg(msg)}{default_msg}"
        return self.soft_assert_true(
            obj is None, error, with_screen=with_screen, hard_assert=hard_assert
        )

    def soft_assert_is_not_none(
        self,
        obj: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that object is not None."""
        default_msg = "" if msg else "Unexpectedly None.\n"
        error = f"{base_msg(msg)}{default_msg}"
        return self.soft_assert_true(
            obj is not None,
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_is_instance(
        self,
        obj: Any,
        cls: Any,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that object is instance of given class."""
        default_msg = "" if msg else f"{obj} is not an instance of {cls}.\n"
        error = f"{base_msg(msg)}{default_msg}"
        return self.soft_assert_true(
            isinstance(obj, cls),
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_equals_text_with_ignore_spaces_and_register(
        self,
        current_text: str,
        expected_text: str,
        msg: str = "Invalid checked text.",
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Compare texts ignoring spaces and case."""
        current = get_text_with_ignore_whitespace_symbols(current_text)
        expected = get_text_with_ignore_whitespace_symbols(expected_text)
        if not current:
            msg = "Warning: current text is None!"
        self.soft_assert_equals(
            current.lower(),
            expected.lower(),
            f"{msg}\nCurrent text without formatting: {current_text}"
            f"\nExpected text without formatting: {expected_text}",
            show_diff=False,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_schemas(
        self,
        current: dict,
        expected: dict,
        msg: str = "",
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Validate dictionary schema using json_checker."""
        try:
            Checker(expected, soft=True).validate(current)
        except CheckerError as e:
            error = f"{msg}\n{e}\n"
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )
            return error
        return None

    def assert_keys_and_instances(
        self,
        actual_dict: dict,
        expected_dict: dict,
        can_be_null: list | None = None,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that dict keys and value types match expected."""
        assert actual_dict, "Actual dict is empty, check your data"

        self.soft_assert_equals(
            sorted(iter(actual_dict.keys())),
            sorted(iter(expected_dict.keys())),
            "Wrong keys list.",
            with_screen=with_screen,
            hard_assert=hard_assert,
        )
        for actual_key, actual_value in actual_dict.items():
            self.soft_assert_in(
                member=actual_key,
                container=expected_dict,
                msg=f'Not expected key "{actual_key}".',
                with_screen=with_screen,
                hard_assert=hard_assert,
            )
            if actual_key in expected_dict:
                expected_value = (
                    type(None)
                    if actual_value is None and actual_key in (can_be_null or [])
                    else expected_dict[actual_key]
                )
                message = f"({msg})" if msg else ""
                self.soft_assert_true(
                    expr=isinstance(actual_value, expected_value),
                    msg=(
                        f"Wrong object instance class.\n"
                        f'Key "{actual_key}" value is "{type(actual_value)}", '
                        f'expected "{expected_value}". {message}'
                    ),
                    with_screen=with_screen,
                    hard_assert=hard_assert,
                )

    def soft_assert_dicts_with_ignore_types(
        self,
        current: Any,
        expected: Any,
        msg: str = "",
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Compare two dicts ignoring value types."""
        expected_dict = _check_namedtuple(expected)
        current_dict = _check_namedtuple(current)
        errors = ""
        for actual_key, actual_value in current_dict.items():
            if actual_key in expected_dict:
                if str(actual_value) != str(expected_dict[actual_key]):
                    errors += (
                        f"\nKey {actual_key} "
                        f"\nHas incorrect value: {actual_value}  "
                        f"Expected: {expected_dict[actual_key]} \n"
                    )
        if errors:
            error = (
                f"{msg}{errors}"
                f"\nExpected dict: {convert_container(expected_dict)}"
                f"\nCurrent dict: {convert_container(current_dict)}"
            )
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )

    def soft_assert_equal_dict_from_clerk_magic(
        self,
        current_dict: dict,
        expected_dict: dict,
        msg: str | None = None,
        coerce: CoerceDict = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Compare dicts by type, coercing values if needed."""

        def _equal(
            field_name: str, current: str, expected: str, type_coerce: CoerceDict
        ) -> bool:
            if type_coerce is not None and field_name in type_coerce:
                cast = type_coerce[field_name]
                return cast(current) == cast(expected)
            if type(current) is type(expected):
                return current == expected
            return str(current) == str(expected)

        missing = []
        unequal = []
        for key, value in expected_dict.items():
            if key not in current_dict:
                missing.append((key, value))
            elif not _equal(key, value, current_dict[key], coerce):
                unequal.append((
                    key,
                    f"\n\t\tproduct_data - '{value}'"
                    f" != analytic_data - '{current_dict[key]}'",
                ))

        unequal_check = "\n\t".join([":".join(map(str, a)) for a in unequal])
        missing_check = "\n\t".join([":".join(map(str, a)) for a in missing])
        self.soft_assert_true(
            (missing, unequal) == ([], []),
            msg=(
                f"{base_msg(msg)}\n"
                f"Unequal_keys:\n\t{unequal_check}\n"
                f"\nMissed_keys:\n\t[{missing_check}]"
            ),
            with_screen=with_screen,
            hard_assert=hard_assert,
        )


class RequestSoftAssertion(BaseSoftAssertion):
    """Soft assertions for request-based checks."""

    @property
    def url(self) -> str:
        """Return current URL from session."""
        return self.session.url

    def base_msg(self, msg: str | None = None) -> str:
        """Return formatted message including URL and optional extra message."""
        url = f"\n{self.url}" if self.url else ""
        exception = f"\n{msg}" if msg else ""
        return f"{url}{exception}"


class WebDriverSoftAssertion(BaseSoftAssertion):
    """Soft assertions for WebDriver-based checks."""

    _driver: SeleniumWebDriver | None = None

    @property
    def driver(self) -> SeleniumWebDriver | None:
        return self._driver

    @driver.setter
    def driver(self, value: SeleniumWebDriver | None) -> None:
        self._driver = value

    @property
    def url(self) -> str:
        """Return current browser URL."""
        return self.driver.current_url if self.driver else ""

    def base_msg(
        self, default_msg: str | None = None, extend_msg: str | None = None
    ) -> str:
        """Return formatted message including default, extended, and URL."""
        default = f"Default message: {default_msg}\n" if default_msg else ""
        extend = f"Extend message: {extend_msg}\n" if extend_msg else ""
        return f"{default}{extend}\nURL: {self.url}"

    def soft_assert_page_title(
        self,
        expected_title: str,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that page title matches expected."""
        default_msg = "Wrong page title."
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_equals(
            self.driver.title if self.driver else None,
            expected_title,
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_current_url(
        self,
        expected_url: str,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that current URL matches expected."""
        default_msg = "Wrong current url."
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_equals(
            self.url,
            expected_url,
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_current_url_contains(
        self,
        url_mask: str,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that current URL contains mask."""
        default_msg = f"URL {str(self.url)} doesn't contain {str(url_mask)}."
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_in(
            url_mask,
            self.url,
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_current_url_not_contains(
        self,
        url_mask: str,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that current URL does not contain mask."""
        default_msg = f"URL {str(self.url)} contains {str(url_mask)}."
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_not_in(
            url_mask,
            self.url,
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_element_is_present(
        self,
        element: Any,
        msg: str | None = None,
        *,
        with_screen: bool = True,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that element is present in DOM."""
        default_msg = (
            f"Element {element.by}={element.locator} is not present"
            f" on page at current time."
        )
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_true(
            element.is_present(),
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_element_is_not_present(
        self,
        element: Any,
        msg: str | None = None,
        *,
        with_screen: bool = True,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that element is not present in DOM."""
        default_msg = f"Element {element.by}={element.locator} is found on page."
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_false(
            element.is_present(),
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_element_is_displayed(
        self,
        element: Any,
        msg: str | None = None,
        *,
        with_screen: bool = True,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that element is visible to user."""
        default_msg = (
            f"Element {element.by}={element.locator} is not visible to a user."
        )
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_true(
            element.is_displayed(),
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_element_is_not_displayed(
        self,
        element: Any,
        msg: str | None = None,
        *,
        with_screen: bool = True,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that element is not visible to user."""
        default_msg = (
            f"Element {element.by}={element.locator} is visible to a user."
        )
        error = f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}"
        self.soft_assert_false(
            element.is_displayed(),
            error,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )

    def soft_assert_element_displayed_in_viewport(
        self,
        element: Any,
        msg: str | None = None,
        *,
        with_screen: bool = True,
        hard_assert: bool | None = None,
    ) -> None:
        """Check that element is inside viewport."""
        element_in_viewport = self.driver.execute_script(
            """
            function elementInViewport(el) {
                var top = el.offsetTop;
                var left = el.offsetLeft;
                var width = el.offsetWidth;
                var height = el.offsetHeight;

                while(el.offsetParent) {
                  el = el.offsetParent;
                  top += el.offsetTop;
                  left += el.offsetLeft;
                }
                return (
                    top >= window.pageYOffset &&
                    left >= window.pageXOffset &&
                    (top + height) <= (
                        window.pageYOffset + window.innerHeight
                    ) &&
                    (left + width) <= (
                        window.pageXOffset + window.innerWidth
                    )
                );
            }
            element = arguments[0];
            return elementInViewport(element);
            """,
            element.lookup(),
        )

        if element_in_viewport is not True:
            default_msg = (
                f"Element {element.by}={element.locator}"
                f" not displayed in viewport"
            )
            error = (
                f"{self.base_msg(default_msg=default_msg, extend_msg=msg)}\n\n"
            )
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )

    def soft_assert_image_status_code(
        self,
        image: Any,
        status_code: int = 200,
        msg: str | None = None,
        *,
        with_screen: bool = False,
        hard_assert: bool | None = None,
    ) -> str | None:
        """Check that image URL returns expected status code."""
        if not image.get_attribute("src"):
            error = f"{base_msg(msg)}Image does not have attribute 'src'\n"
            self._emit(
                error, with_screen=with_screen, hard_assert_override=hard_assert
            )
            return error

        img_url = image.get_attribute("src")
        response = http.request(url=img_url, method="GET")
        assert_msg = msg if msg else "img status code != 200"
        return self.soft_assert_equals(
            response.status,
            status_code,
            msg=assert_msg,
            with_screen=with_screen,
            hard_assert=hard_assert,
        )
