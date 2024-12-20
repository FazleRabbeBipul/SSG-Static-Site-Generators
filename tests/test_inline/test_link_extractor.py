import unittest
from src.inline.link_extractor import extract_markdown_links

class TestLinkExtractor(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_no_links(self):
        text = "No links here"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_links_with_special_characters(self):
        text = "This is a link [Google](https://www.google.com/search?q=test) and another [Search](https://www.search.com?q=python)"
        expected = [('Google', 'https://www.google.com/search?q=test'), ('Search', 'https://www.search.com?q=python')]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == '__main__':
    unittest.main()
