import unittest
from src.text_alignment.util import text_adjustment

class Test_Text_Ajustment(unittest.TestCase):
    def test_text_adjustment(self):
        expected_output = (
            "     H     \n"
            "    HHH    \n"
            "   HHHHH   \n"
            "  HHHHHHH  \n"
            " HHHHHHHHH \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n"
            "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n"
            "  HHHHHHHHHHHHHHHHHHHHHHHHH   \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "  HHHHH               HHHHH  \n"
            "                    HHHHHHHHH \n"
            "                     HHHHHHH  \n"
            "                      HHHHH   \n"
            "                       HHH    \n"
            "                        H      \n"
        )

        output = text_adjustment(5)
        # Print the actual output and expected output for comparison
        print("Actual Output:\n", repr(output))
        print("Expected Output:\n", repr(expected_output))

        self.assertEqual(output,expected_output)


if __name__ == "__main__":
    unittest.main()