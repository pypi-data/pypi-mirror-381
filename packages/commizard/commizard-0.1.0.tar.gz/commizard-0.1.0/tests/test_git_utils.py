import subprocess
from unittest.mock import patch

import pytest
from commizard import git_utils


# TODO: add valid test cases that mock actual returns or subprocess.run
@pytest.mark.parametrize(
    "args, mock_result, raised_exception",
    [
        # successful git commands
        (["status"],
         subprocess.CompletedProcess(args=["git", "status"], returncode=0,
                                     stdout="On branch main\n", stderr=""),
         None),
        (["log", "--oneline"],
         subprocess.CompletedProcess(args=["git", "log", "--oneline"],
                                     returncode=0,
                                     stdout="abc123 Initial commit\n",
                                     stderr=""), None),
        # git command failure
        (["push"],
         subprocess.CompletedProcess(args=["git", "push"], returncode=1,
                                     stdout="", stderr="Authentication failed"),
         None),
        # exceptions
        (["status"], None, FileNotFoundError("git not found")),
        (["push"], None,
         subprocess.TimeoutExpired(cmd=["git", "push"], timeout=5)),
    ]
)
@patch("subprocess.run")
def test_run_git_command(mock_run, args, mock_result, raised_exception):
    if raised_exception:
        mock_run.side_effect = raised_exception

    # if the test case didn't raise an exception
    else:
        mock_run.return_value = mock_result

    result = git_utils.run_git_command(args)

    # was subprocess.run called with correct arguments
    mock_run.assert_called_once_with(["git"] + args, capture_output=True,
                                     text=True, encoding='utf-8',
                                     errors='ignore')

    assert result is mock_result


@pytest.mark.parametrize(
    "mock_val, expected_result",
    [
        (subprocess.CompletedProcess(
            args=['git', 'rev-parse', '--is-inside-work-tree'],
            returncode=128, stdout='',
            stderr='fatal: not a git repository (or any of the parent directories): .git\n'),
         False),
        (subprocess.CompletedProcess(
            args=['git', 'rev-parse', '--is-inside-work-tree'], returncode=0,
            stdout='true\n', stderr=''), True),
        (subprocess.CompletedProcess(
            args=['git', 'rev-parse', '--is-inside-work-tree'], returncode=0,
            stdout='false\n', stderr=''), False),
    ]
)
@patch("commizard.git_utils.run_git_command")
def test_is_inside_working_tree(mock_run, mock_val, expected_result):
    mock_run.return_value = mock_val
    res: bool = git_utils.is_inside_working_tree()
    mock_run.assert_called_once_with(["rev-parse", "--is-inside-work-tree"])
    assert res == expected_result


@pytest.mark.parametrize(
    "mock_val, expected",
    [
        # This shouldn't happen based on the code's structure of running
        # is_inside_working_tree at start.
        (subprocess.CompletedProcess(args=['git', 'diff', '--name-only'],
                                     returncode=128, stdout='',
                                     stderr='fatal: this operation must be run in a work tree\n'),
         False),
        (subprocess.CompletedProcess(args=['git', 'diff', '--name-only'],
                                     returncode=0,
                                     stdout='tests/test_git_utils.py\n',
                                     stderr=''),
         True),
        (subprocess.CompletedProcess(args=['git', 'diff', '--name-only'],
                                     returncode=0, stdout='', stderr=''),
         False),
    ]
)
@patch("commizard.git_utils.run_git_command")
def test_is_changed(mock_run, mock_val, expected):
    mock_run.return_value = mock_val
    res = git_utils.is_changed()
    mock_run.assert_called_once_with(["diff", "--name-only"])
    assert res == expected


@pytest.mark.parametrize(
    "mock_val, expected",
    [
        (subprocess.CompletedProcess(args=['git', '--no-pager', 'diff'],
                                     returncode=0, stdout='', stderr=''), ""),
        (subprocess.CompletedProcess(args=['git', '--no-pager', 'diff'],
                                     returncode=0,
                                     stdout='test_out\n',
                                     stderr=''), "test_out"),
    ]
)
@patch("commizard.git_utils.run_git_command")
def test_get_diff(mock_run, mock_val, expected):
    mock_run.return_value = mock_val
    res = git_utils.get_diff()

    if expected == "":
        mock_run.assert_called_once_with(["diff", "--name-only"])
    else:
        mock_run.assert_any_call(["diff", "--name-only"])
        mock_run.assert_any_call(["--no-pager", "diff", "--no-color"])

    assert res == expected


@pytest.mark.parametrize(
    "stdout, stderr, expected_ret",
    [
        ("Commit successful\n", "", "Commit successful"),
        ("   \n", "Some error\n", "Some error"),
        ("   \n", "   \n", ""),
    ],
)
@patch("commizard.git_utils.run_git_command")
def test_commit(mock_run_git_command, stdout, stderr, expected_ret):
    # arrange: directly configure the mock return value
    mock_run_git_command.return_value.stdout = stdout
    mock_run_git_command.return_value.stderr = stderr
    mock_run_git_command.return_value.returncode = 42

    code, output = git_utils.commit("test message")

    mock_run_git_command.assert_called_once_with(
        ["commit", "-a", "-m", "test message"])
    assert code == 42
    assert output == expected_ret


@pytest.mark.parametrize(
    "input_diff, expected_output",
    [
        (
                "diff --git a/file.py b/file.py\nindex abc..def\n+added line\n"
                "-removed line",
                "+added line\n-removed line"
        ),
        (
                "+added line\n-removed line",
                "+added line\n-removed line"
        ),
        (
                "",
                ""
        ),
        (
                "diff --git a/file.py b/file.py\nindex abc..def\n"
                "warning: something",
                ""
        ),
    ]
)
def test_clean_diff(input_diff, expected_output):
    result = git_utils.clean_diff(input_diff)
    assert result == expected_output
