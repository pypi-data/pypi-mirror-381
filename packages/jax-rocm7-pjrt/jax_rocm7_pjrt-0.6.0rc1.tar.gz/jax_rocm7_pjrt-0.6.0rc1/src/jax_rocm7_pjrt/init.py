# Minimal stub: clearly indicate this is not the functional ROCm PJRT package.
def __getattr__(name):
    raise RuntimeError(
        "jax-rocm7-pjrt: this is a minimal stub uploaded to satisfy PyPI’s size-limit process. "
        "It does not contain ROCm binaries. Please install the full wheel when available."
    )

