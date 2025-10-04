##
##-----------------------------------------------------------------------------
##
## Copyright (c) 2023 JEOL Ltd.
## 1-2 Musashino 3-Chome
## Akishima Tokyo 196-8558 Japan
##
## This software is provided under the MIT License. For full license information,
## see the LICENSE file in the project root or visit https://opensource.org/licenses/MIT
##
##++---------------------------------------------------------------------------
##
## ModuleName : BeautifulJASON
## ModuleType : Python API for JASON desktop application and JJH5 documents
## Purpose : Automate processing, analysis, and report generation with JASON
## Author : Nikolay Larin
## Language : Python
##
####---------------------------------------------------------------------------
##

import os
import unittest
import beautifuljason as bjason
from beautifuljason.tests.config import datafile_path, newfile_path
import subprocess
import time
import threading
import random

class JASONTestCase(unittest.TestCase):
    """JASON class test cases"""

    def test_ctor(self):
        with self.assertRaises(OSError):
            _ = bjason.JASON(__file__)
        with self.assertRaises(bjason.JASONException):
            _ = bjason.JASON("")
        with self.assertRaises(bjason.JASONException):
            _ = bjason.JASON("./")

        jason = bjason.JASON()
        self.assertEqual(jason._fixed_args, ["--plugins", "off"])
        self.assertIsInstance(jason, bjason.JASON)

        jason = bjason.JASON(plugins=["on"])
        self.assertEqual(jason._fixed_args, ["--plugins", "on"])

        # Test plugins argument and plugin name normalization
        jason = bjason.JASON(plugins=[])
        self.assertEqual(jason._fixed_args, [])
        jason = bjason.JASON(plugins=["SMILEQ", "MAGRES", "Screening", "Test1"])
        self.assertEqual(jason._fixed_args, ["--plugins", "SmileQ Plugin", "--plugins", "MAGRES File Filter Plugin", "--plugins", "Screening Plugin", "--plugins", "Test1"])
        jason = bjason.JASON(plugins=["SMILEQ Plugin", "MAGRES Plugin", "Screening Plugin", "Test1 Plugin"])
        self.assertEqual(jason._fixed_args, ["--plugins", "SmileQ Plugin", "--plugins", "MAGRES File Filter Plugin", "--plugins", "Screening Plugin", "--plugins", "Test1 Plugin"])

        # Test extra_args argument and argument validation
        jason = bjason.JASON(plugins=["SMILEQ", "MAGRES", "Screening", "Test1"], extra_args=["--test_arg", "value"])
        self.assertEqual(jason._fixed_args, ["--plugins", "SmileQ Plugin", "--plugins", "MAGRES File Filter Plugin", "--plugins", "Screening Plugin", "--plugins", "Test1", "--test_arg", "value"])
        jason = bjason.JASON(plugins=["SMILEQ", "MAGRES", "Screening", "Test1"], extra_args=["--test_arg"])
        self.assertEqual(jason._fixed_args, ["--plugins", "SmileQ Plugin", "--plugins", "MAGRES File Filter Plugin", "--plugins", "Screening Plugin", "--plugins", "Test1", "--test_arg"])
        with self.assertRaises(ValueError):
            jason = bjason.JASON(plugins=["SMILEQ", "MAGRES", "Screening", "Test1"], extra_args=["--test_arg", "value", "another_value"])

    def test_version(self):
        jason = bjason.JASON()
        version = jason.version
        self.assertEqual(len(version), 3)
        self.assertIsInstance(version, tuple)
        self.assertIsInstance(version[0], int)
        self.assertIsInstance(version[1], int)
        self.assertIsInstance(version[2], int)

    def test_create_document(self):
        jason = bjason.JASON()
        with jason.create_document([
                datafile_path('Ethylindanone_Proton-13-1.jdf'),
                datafile_path('Ethylindanone_Carbon-3-1.jdf'),
                datafile_path('Ethylindanone_HMQC-1-1.jdf')]) as doc:
            self.assertEqual(len(doc.items), 3)
            self.assertEqual(len(doc.nmr_items), 3)
            self.assertEqual(len(doc.nmr_data), 3)
            self.assertEqual(len(doc.mol_data), 0)
            self.assertEqual(len(doc.image_data), 0)
            self.assertEqual(len(doc.text_data), 0)

        with jason.create_document([]) as doc:
            self.assertEqual(len(doc.items), 0)
            self.assertEqual(len(doc.nmr_items), 0)
            self.assertEqual(len(doc.nmr_data), 0)
            self.assertEqual(len(doc.mol_data), 0)
            self.assertEqual(len(doc.image_data), 0)
            self.assertEqual(len(doc.text_data), 0)

    def test__run(self):
        """Test the _run method"""
        jason = bjason.JASON()
        save_path = newfile_path("test_run_output.jjh5")
        self.assertFalse(os.path.exists(save_path))
        runres = jason._run([
                datafile_path('Ethylindanone_Proton-13-1.jdf'),
                datafile_path('Ethylindanone_Carbon-3-1.jdf'),
                datafile_path('Ethylindanone_HMQC-1-1.jdf'),
                "--save", save_path])
        self.assertEqual(runres.returncode, 0)
        with bjason.Document(save_path, is_temporary=True) as doc:
            self.assertEqual(len(doc.items), 3)
            self.assertEqual(len(doc.nmr_items), 3)
            self.assertEqual(len(doc.nmr_data), 3)
            self.assertEqual(len(doc.mol_data), 0)
            self.assertEqual(len(doc.image_data), 0)
            self.assertEqual(len(doc.text_data), 0)
        self.assertFalse(os.path.exists(save_path))

    def test__run_background(self):
        """Test the _run_background method"""
        jason = bjason.JASON()
        with self.assertRaises(bjason.JASONException):
            _ = jason._run_background(["--dummy"])  # Missing --appid
        jason_process = jason._run_background(["--appid", "test_jason_server"])
        self.assertIsNotNone(jason_process)
        self.assertIsInstance(jason_process, subprocess.Popen)
        self.assertIsNotNone(jason_process.pid)
        # Send commands to the background JASON instance
        save_path = newfile_path("test_run_output_server.jjh5")
        self.assertFalse(os.path.exists(save_path))
        jason._run([
                datafile_path('Ethylindanone_Proton-13-1.jdf'),
                datafile_path('Ethylindanone_Carbon-3-1.jdf'),
                datafile_path('Ethylindanone_HMQC-1-1.jdf'),
                "--save", save_path,
                "--appid", "test_jason_server"])
        # Wait for the file to be saved
        jason._wait_for_file(save_path)
        self.assertTrue(os.path.exists(save_path))
        # Quit the background JASON instance in a separate command to ensure clean shutdown
        jason._run(["--quit", "--appid", "test_jason_server"])
        # Wait for the background process to terminate
        jason_process.wait(timeout=30)
        self.assertIsNotNone(jason_process.returncode)
        self.assertEqual(jason_process.returncode, 0)
        with bjason.Document(save_path, is_temporary=True) as doc:
            self.assertEqual(len(doc.items), 3)
            self.assertEqual(len(doc.nmr_items), 3)
            self.assertEqual(len(doc.nmr_data), 3)
            self.assertEqual(len(doc.mol_data), 0)
            self.assertEqual(len(doc.image_data), 0)
            self.assertEqual(len(doc.text_data), 0)
        self.assertFalse(os.path.exists(save_path))

    def test__wait_for_file(self):
        """Test the _wait_for_file method."""
        jason = bjason.JASON()
        # Test waiting for a file that appears and stabilizes
        save_path = newfile_path("test_wait_for_file.jjh5")
        self.assertFalse(os.path.exists(save_path))

        def create_file_later(path: str, delay: float, content: bytes):
            time.sleep(delay)
            with open(path, 'wb') as f:
                f.write(content)

        threading.Thread(target=create_file_later, args=(save_path, 1.0, b'Test content')).start()
        jason._wait_for_file(save_path)
        self.assertTrue(os.path.exists(save_path))
        with open(save_path, 'rb') as f:
            content = f.read()
        self.assertEqual(content, b'Test content')
        os.remove(save_path)

        # Test waiting for a file that does not appear (should timeout)
        with self.assertRaises(TimeoutError):
            jason._wait_for_file(newfile_path("non_existent_file.jjh5"), timeout=2)

        # Test waiting for a file that appears but does not stabilize (should timeout)
        unstable_path = newfile_path("unstable_file.jjh5")
        self.assertFalse(os.path.exists(unstable_path))

        def create_unstable_file(path: str, interval: float, iterations: int):
            for _ in range(iterations):
                with open(path, 'wb') as f:
                    # Write random content of random size to simulate real instability
                    f.write(os.urandom(random.randint(8, 32)))
                # Randomize interval slightly to avoid predictable stabilization
                time.sleep(interval + random.uniform(0, 0.005))
            # After instability, leave the file for a short time before removal
            time.sleep(0.1)
            os.remove(path)  # Clean up after

        # The file will be modified for 0.5 seconds, so set timeout < 0.5 to guarantee a timeout
        # The file will be modified for 10 seconds, so set timeout < 10 to guarantee a timeout
        thread = threading.Thread(target=create_unstable_file, args=(unstable_path, 0.01, 1000))
        thread.start()
        with self.assertRaises(TimeoutError):
            jason._wait_for_file(unstable_path, timeout=2)
        thread.join()  # Ensure the file is no longer in use
        if os.path.exists(unstable_path):
            os.remove(unstable_path)

if __name__ == '__main__':
    unittest.main()
