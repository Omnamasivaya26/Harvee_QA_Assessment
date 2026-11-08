from pathlib import Path
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot automatically when a test call fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            screenshot_dir = Path("artifacts/screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            safe_name = "".join(
                char if char.isalnum() or char in ("-", "_") else "_"
                for char in item.nodeid
            )
            try:
                page.screenshot(
                    path=str(screenshot_dir / f"{safe_name}.png"),
                    full_page=True
                )
            except Exception as exc:
                # Preserve the original test failure if screenshot capture fails.
                print(f"Could not capture failure screenshot: {exc}")
