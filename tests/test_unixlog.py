from unixlog.ulog import apply_color, info, warning, error, success, debug, trace
import unittest


class TestCharts(unittest.TestCase):
    def setUp(self):
        self.text = "Hello Unix Log utility"

    def test_unixlog_apply_color_function(self):
        assert "Hello" in apply_color("info", self.text)

    def test_unixlog_warning_function(self):
        assert 'WARNING' in warning(self.text)

    def test_unixlog_info_function(self):
        assert 'INFO' in info(self.text)

    def test_unixlog_error_function(self):
        assert 'ERROR' in error(self.text)

    def test_unixlog_success_function(self):
        assert 'SUCCESS' in success(self.text)

    def test_unixlog_debug_function(self):
        assert 'DEBUG' in debug(self.text)

    def test_unixlog_trace_function(self):
        assert 'TRACE' in trace(self.text)
