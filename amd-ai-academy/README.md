# AMD AI Academy

This repository contains my coursework from the **AMD AI Academy** - a course I took to learn the fundamentals of **Triton** and **GPU kernel development** on AMD Instinct GPUs.

## Course Overview

[OpenAI Triton](https://github.com/triton-lang/triton) is a Python-based programming language and compiler designed to write highly efficient GPU kernels with performance comparable to hand-tuned HIP/CUDA code. This course demonstrates how to develop Triton kernels specifically on AMD Instinct GPUs.

## Contents

### [Triton Kernel Development on AMD Instinct GPUs](ai_academy_triton_kernel_development.ipynb)

This notebook covers:

- **Environment Setup**: Setting up the Triton development environment using ROCm PyTorch images on AMD MI GPUs
- **Installation**: Installing OpenAI Triton from source for optimal performance
- **Vector Add Kernel**: Developing a first Triton kernel with:
  - Naive implementation
  - Performance benchmarking
  - Autotune optimization for different block sizes and configurations
- **Reduce Kernel**: Implementing reduction operations (summing vector elements):
  - Naive reduction with atomic operations
  - Correctness validation against PyTorch
  - Performance benchmarking

## Key Concepts Learned

1. **Triton JIT Compilation**: Using `@triton.jit` decorator to compile Python functions into GPU code
2. **Block-Based Processing**: Understanding how GPU programs process data in blocks
3. **Memory Coalescing**: Optimizing memory access patterns for GPU efficiency
4. **Autotuning**: Using `@triton.autotune` to automatically find optimal configurations
5. **Atomic Operations**: Handling race conditions in parallel reductions
6. **Performance Benchmarking**: Comparing Triton kernels against PyTorch operations

## Resources

- [AMD Developer Cloud](https://amd.digitalocean.com/) - Access to AMD Instinct GPU cloud instances
- [OpenAI Triton Repository](https://github.com/triton-lang/triton) - Official Triton source and documentation
- [Triton Issues](https://github.com/triton-lang/triton/issues) - For reporting build or usage issues

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
