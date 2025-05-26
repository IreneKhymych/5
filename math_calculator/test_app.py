import io
import unittest
from app import app, allowed_file

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_allowed_file(self):
        self.assertTrue(allowed_file("file.json"))
        self.assertTrue(allowed_file("data.XML"))
        self.assertFalse(allowed_file("note.txt"))
        self.assertFalse(allowed_file("archive.zip"))

    def test_upload_no_file(self):
        response = self.app.post('/upload', data={})
        self.assertEqual(response.status_code, 302)

    def test_wrong_extension(self):
        data = {'taskfile': (io.BytesIO(b"dummy content"), 'file.txt')}
        response = self.app.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
