"""
Python equivalent of js-source/conflicts-across-class-groups.test.ts
Last synced with original version: Current (as of implementation)

This test file maintains exact parity with the TypeScript tests to ensure
consistent behavior between the JavaScript and Python implementations.
"""

import pytest
from starmerge import merge


def test_handles_conflicts_across_class_groups_correctly():
    """Equivalent to the 'handles conflicts across class groups correctly' test in TypeScript."""
    assert merge('inset-1 inset-x-1') == 'inset-1 inset-x-1'
    assert merge('inset-x-1 inset-1') == 'inset-1'
    assert merge('inset-x-1 left-1 inset-1') == 'inset-1'
    assert merge('inset-x-1 inset-1 left-1') == 'inset-1 left-1'
    assert merge('inset-x-1 right-1 inset-1') == 'inset-1'
    assert merge('inset-x-1 right-1 inset-x-1') == 'inset-x-1'
    assert merge('inset-x-1 right-1 inset-y-1') == 'inset-x-1 right-1 inset-y-1'
    assert merge('right-1 inset-x-1 inset-y-1') == 'inset-x-1 inset-y-1'
    assert merge('inset-x-1 hover:left-1 inset-1') == 'hover:left-1 inset-1'


def test_ring_and_shadow_classes_do_not_create_conflict():
    """Equivalent to the 'ring and shadow classes do not create conflict' test in TypeScript."""
    assert merge('ring shadow') == 'ring shadow'
    assert merge('ring-2 shadow-md') == 'ring-2 shadow-md'
    assert merge('shadow ring') == 'shadow ring'
    assert merge('shadow-md ring-2') == 'shadow-md ring-2'


def test_touch_classes_do_create_conflicts_correctly():
    """Equivalent to the 'touch classes do create conflicts correctly' test in TypeScript."""
    assert merge('touch-pan-x touch-pan-right') == 'touch-pan-right'
    assert merge('touch-none touch-pan-x') == 'touch-pan-x'
    assert merge('touch-pan-x touch-none') == 'touch-none'
    assert merge('touch-pan-x touch-pan-y touch-pinch-zoom') == 'touch-pan-x touch-pan-y touch-pinch-zoom'
    assert merge('touch-manipulation touch-pan-x touch-pan-y touch-pinch-zoom') == 'touch-pan-x touch-pan-y touch-pinch-zoom'
    assert merge('touch-pan-x touch-pan-y touch-pinch-zoom touch-auto') == 'touch-auto'


def test_line_clamp_classes_do_create_conflicts_correctly():
    """Equivalent to the 'line-clamp classes do create conflicts correctly' test in TypeScript."""
    assert merge('overflow-auto inline line-clamp-1') == 'line-clamp-1'
    assert merge('line-clamp-1 overflow-auto inline') == 'line-clamp-1 overflow-auto inline' 