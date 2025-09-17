import os
import shutil
import unittest
from core.session import Session
from core.publisher import Publisher
from agents.simple_agent import SimpleAgent

class TestFeatures(unittest.TestCase):

    def setUp(self):
        """Set up a clean environment for each test."""
        self.db_path = ".test_chroma"
        self.notes_path = "test_starlight-notes"
        # Clean up previous test runs
        if os.path.exists(self.db_path):
            shutil.rmtree(self.db_path)
        if os.path.exists(self.notes_path):
            shutil.rmtree(self.notes_path)

    def tearDown(self):
        """Clean up the environment after each test."""
        if os.path.exists(self.db_path):
            shutil.rmtree(self.db_path)
        if os.path.exists(self.notes_path):
            shutil.rmtree(self.notes_path)

    def test_integration(self):
        """
        Tests the full workflow:
        1. Agent interaction logs to ChromaDB.
        2. Memory can be searched.
        3. Session can be published to a Markdown file.
        """
        # 1. Agent interaction
        session = Session(store_path=self.db_path)
        agent = SimpleAgent(session=session)
        agent.interact(["Hello, world!", "This is a test."])

        # 2. Memory search
        search_results = session.store.search("test message", n_results=1)
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].text, "This is a test.")

        # 3. Publish session
        publisher = Publisher(output_dir=self.notes_path)
        filepath = publisher.publish_session(session)

        # Verify publication
        self.assertTrue(os.path.exists(filepath))
        with open(filepath, "r") as f:
            content = f.read()
            self.assertIn("Hello, world!", content)
            self.assertIn("This is a test.", content)
            self.assertIn("AGENT_RESPONSE", content)

if __name__ == "__main__":
    unittest.main()
