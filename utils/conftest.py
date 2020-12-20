import pytest


def pytest_html_report_title(report):
    report.title = "ASSESSMENT REPORT"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["Course"] = "DSML"


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append("You passed this test!")
