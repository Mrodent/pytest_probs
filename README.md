# pytest_probs
illustrates difficulties with import of sibling .py files during pytest run

2023-08-21

so... as per the problem and my answer here: https://stackoverflow.com/a/69691436/595305

The problem is:

Currently, running "pytest" should result in a run... 3 out of 4 tests in test_basic will fail, as intended.

Now comment out, in conftest.py, the line 
sys.path.insert(0, src_core_dir_path_str)

... this line obviously manually adds "src/core" to the sys.path. 

After commenting out this line, in my setup, pytest 7.3.1, means a ModuleNotFound error on line "import bubble" in __main__.py during a pytest run.

But bubble.py is a sibling .py file of __main__.py! It should be able to be imported!
