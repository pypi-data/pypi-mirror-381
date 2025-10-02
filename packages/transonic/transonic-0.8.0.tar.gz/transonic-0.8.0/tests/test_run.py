import os
import sys
import time

import pytest

from transonic import util
from transonic.config import backend_default
from transonic.mpi import nb_proc
from transonic.testing import path_data_tests
from transonic.run import run


header_suffixes = {"pythran": ".pythran", "cython": ".pxd"}


@pytest.mark.skipif(not path_data_tests.exists(), reason="no data tests")
@pytest.mark.skipif(nb_proc > 1, reason="No commandline in MPI")
def test_create_pythran_files(path_input_files):

    if os.name != "nt":
        sys.argv = f"transonic -nc {path_input_files / '*.py'}".split()
        run()

    sys.argv = f"transonic -nc {path_input_files}".split()
    run()

    paths = tuple(path_input_files.glob("*.py*"))
    sys.argv = ["transonic", "-nc"] + [str(path) for path in paths]
    run()

    # At this point, we can compare the produced files with saved files.
    # For exterior files, we can't compare cause transonic changes their names
    no_compare = [
        "no_pythran_.py",
        "assign_func_jit.py",
        "exterior_import_boost.py",
        "exterior_import_boost_2.py",
    ]

    dir_saved_files = "saved__backend__"

    for path in paths:
        if path.name in no_compare:
            continue

        __backend__path = path.parent / f"__{backend_default}__" / path.name
        assert __backend__path.exists()

        saved_path = (
            path_data_tests / dir_saved_files / backend_default / path.name
        )
        assert saved_path.exists()

        with open(__backend__path) as file:
            code = file.read()
        with open(saved_path) as file:
            saved_code = file.read()

        if sys.version_info[:2] < (3, 11):
            if path.name == "subpackages.py":
                saved_code = saved_code.replace("nx, ny =", "(nx, ny) =")

        code = code.split("def __transonic__():", 1)[0]
        saved_code = saved_code.split("def __transonic__()", 1)[0]

        if backend_default in header_suffixes:
            suffix = header_suffixes[backend_default]

            header_path = __backend__path.with_suffix(suffix)
            assert header_path.exists()
            with open(header_path) as file:
                code += file.read()

            header_path = saved_path.with_suffix(suffix)
            assert header_path.exists()
            with open(header_path) as file:
                saved_code += file.read()

        # warning: it is a very strong requirement!
        assert code == saved_code, f"Issue with {path}\nsaved_path = {saved_path}"


@pytest.mark.skipif(not path_data_tests.exists(), reason="no data tests")
@pytest.mark.skipif(nb_proc > 1, reason="No commandline in MPI")
def test_create_pythran_simple():
    sys.argv = "transonic --version".split()
    run()

    sys.argv = ["transonic"]
    run()


@pytest.mark.skipif(not path_data_tests.exists(), reason="no data tests")
@pytest.mark.skipif(nb_proc > 1, reason="No commandline in MPI")
def test_create_trans_classic(path_input_files):
    util.input = lambda: "y"

    path_file = path_input_files / "classic.py"
    sys.argv = f"transonic -nc {path_file}".split()
    run()

    print("after first build")
    run()

    time.sleep(0.02)
    path_file.touch()
    print("after touch")

    run()

    path_file_pythran = path_input_files / f"__{backend_default}__/classic.py"
    path_file_pythran.unlink()

    print("after unlink")
    run()

    sys.argv = f"transonic -cc {path_file}".split()
    run()

    sys.argv = f"transonic {path_file}".split()
    run()

    sys.argv = f"transonic -nc {path_file_pythran}".split()
    run()


@pytest.mark.skipif(not path_data_tests.exists(), reason="no data tests")
@pytest.mark.skipif(nb_proc > 1, reason="No commandline in MPI")
def test_create_pythran_subpackages(path_input_files):
    path_file = path_input_files / "subpackages.py"
    sys.argv = f"transonic -nc {path_file}".split()
    run()
