import unittest
from types import SimpleNamespace
from unittest.mock import patch

from assorted_tools.misc import newsection


class NewsectionTests(unittest.TestCase):
    def test_title_still_waits_before_printing(self):
        events = []

        def record_sleep(delay):
            events.append(("sleep", delay))

        def record_print(*args, **kwargs):
            events.append(("print", None))

        with (
            patch("assorted_tools.misc.sleep", side_effect=record_sleep),
            patch(
                "assorted_tools.misc.shutil.get_terminal_size",
                return_value=SimpleNamespace(columns=80),
            ),
            patch("assorted_tools.misc.centerprint", return_value="section title"),
            patch("builtins.print", side_effect=record_print),
        ):
            newsection(title="section title", delay=3)

        self.assertEqual(events, [("sleep", 3), ("print", None)])

    def test_untitled_section_keeps_its_delay(self):
        with (
            patch("assorted_tools.misc.sleep") as sleep,
            patch(
                "assorted_tools.misc.shutil.get_terminal_size",
                return_value=SimpleNamespace(columns=80),
            ),
            patch("builtins.print"),
        ):
            newsection(delay=2)

        sleep.assert_called_once_with(2)


if __name__ == "__main__":
    unittest.main()
