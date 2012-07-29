__author__ = 'James Polera'
__since__ = '2012.05.29'
__email__ = 'james@uncryptic.com'

try:
  import unittest2 as unittest
except ImportError:
  import unittest

from nameparts import  Name


class TestSimpleName(unittest.TestCase):

  def setUp(self):
    self.name = Name("James Polera")

  def test_split(self):
    "Make sure name is split into discrete parts"

    self.assertTrue("James" == self.name.first_name)
    self.assertTrue("Polera" == self.name.last_name)

  def test_instance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)


class TestComplexName(unittest.TestCase):

  def setUp(self):
    self.name = Name("Otto von Bismark")

  def test_split(self):
    "Make sure name is split into discrete parts"
    self.assertTrue("Otto" == self.name.first_name)
    self.assertTrue("von Bismark" == self.name.last_name)

  def test_isnstance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)


class TestGenerationName(unittest.TestCase):

  def setUp(self):
    self.name = Name("Thurston Howell the 3rd")

  def test_split(self):
    "Make sure name is split into discrete parts"
    self.assertTrue("Thurston" == self.name.first_name)
    self.assertTrue("Howell" == self.name.last_name)
    self.assertTrue("3rd" == self.name.generation)

  def test_isinstance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)


class TestNonNameDataName(unittest.TestCase):

  def setUp(self):
    self.name = Name("Bruce Wayne a/k/a Batman")

  def test_split(self):
    "Make sure that name is split into discrete parts"
    self.assertTrue("Bruce" == self.name.first_name)
    self.assertTrue("Wayne" == self.name.last_name)

  def test_isinstance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)


class TestMultipleMiddleName(unittest.TestCase):

  def setUp(self):
    self.name  = Name("George Herbert Walker Bush")

  def test_split(self):
    "Make sure that name is split into discrete parts"
    self.assertTrue("George" == self.name.first_name)
    self.assertTrue("Herbert Walker" == self.name.middle_name)
    self.assertTrue("Bush" == self.name.last_name)

  def test_isinstance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)

class TestNameWithExtraneousInfo(unittest.TestCase):

  def setUp(self):
    self.name = Name("John Doe fictitious husband of Jane Doe")

  def test_split(self):
    "Make sure that name is split into discrete parts"
    self.assertTrue("John" == self.name.first_name)
    self.assertTrue("Doe" == self.name.last_name)
    self.assertFalse("fictitious" in self.name.as_dict.values())

  def test_isinstance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)

class TestPrefixedLastName(unittest.TestCase):
  def setUp(self):
    "Long name with Prefixes Last Name"
    self.name = Name("Saleh ibn Tariq ibn Khalid al-Fulan")
    self.assertTrue("Saleh" == self.name.first_name)
    self.assertTrue("ibn Tariq ibn Khalid al-Fulan" == self.name.last_name)

  def test_isinstance(self):
    "Test that self.name is an instance of Name"
    self.assertIsInstance(self.name, Name)

if __name__ == '__main__':
  unittest.main()
