import unittest
from src.inline.markdown_extractor import extract_markdown_images

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an image ![image alt text](https://i.imgur.com/aKaOqIh.gif) and another ![another](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("image alt text", "https://i.imgur.com/aKaOqIh.gif"), ("another", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_no_images(self):
        text = "No images here"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_images_with_special_characters(self):
        text = "This is an image ![Google logo](https://www.google.com/images/branding/googlelogo/1x/googlelogo-color-272x92dp.png)"
        expected = [("Google logo", "https://www.google.com/images/branding/googlelogo/1x/googlelogo-color-272x92dp.png")]
        self.assertEqual(extract_markdown_images(text), expected)

if __name__ == '__main__':
    unittest.main()
