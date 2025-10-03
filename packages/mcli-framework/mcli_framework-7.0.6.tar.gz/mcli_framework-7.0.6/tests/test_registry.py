import pytest
from click.testing import CliRunner
from mcli.workflow.registry.registry import registry
import os
from pathlib import Path


def test_registry_group_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['--help'])
    assert result.exit_code == 0
    assert 'registry utility' in result.output


def test_catalog_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['catalog', '--help'])
    assert result.exit_code == 0
    assert 'Fetch the catalog of repositories' in result.output


def test_tags_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['tags', '--help'])
    assert result.exit_code == 0
    assert 'Fetch the tags for a given repository' in result.output


def test_tags_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['tags'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_search_tags_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['search-tags', '--help'])
    assert result.exit_code == 0
    assert 'Fetch the tags for a given repository' in result.output


def test_search_tags_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['search-tags'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_search_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['search', '--help'])
    assert result.exit_code == 0
    assert 'Search for a repository by name' in result.output


def test_search_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['search'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_image_info_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['image-info', '--help'])
    assert result.exit_code == 0
    assert 'Get detailed information about a specific image' in result.output


def test_image_info_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['image-info'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_count_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['count', '--help'])
    assert result.exit_code == 0
    assert 'Count the number of tags/images in a repository' in result.output


def test_count_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['count'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_pull_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['pull', '--help'])
    assert result.exit_code == 0
    assert 'Pull an image from the registry' in result.output


def test_pull_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['pull'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output


def test_fuzzy_search_help():
    runner = CliRunner()
    result = runner.invoke(registry, ['fuzzy-search', '--help'])
    assert result.exit_code == 0
    assert 'TOKEN' in result.output


def test_fuzzy_search_missing_required():
    runner = CliRunner()
    result = runner.invoke(registry, ['fuzzy-search'])
    assert result.exit_code != 0
    assert 'Missing argument' in result.output 