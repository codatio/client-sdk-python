"""Leaf modules holding Speakeasy-name compat enums. Nothing here imports from the
package, so a flat model can import these without triggering models/shared/__init__
(which re-exports flat models and would form an import cycle)."""
