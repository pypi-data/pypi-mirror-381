=========
Changelog
=========

All notable changes to QuScope will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[0.1.0] - 2025-07-09
=====================

**🎉 Initial Release**

Added
-----

**Core Functionality**
- Quantum image encoding with multiple methods (amplitude, angle, basis, FRQI)
- Quantum backend management for simulators and real quantum hardware
- EELS (Electron Energy Loss Spectroscopy) quantum processing tools
- Quantum machine learning modules for microscopy applications

**Image Processing**
- ``quscope.image_processing.quantum_encoding`` - Core quantum image encoding functions
- ``quscope.image_processing.preprocessing`` - Classical image preprocessing utilities  
- ``quscope.image_processing.filtering`` - Quantum and classical filtering operations
- ``quscope.image_processing.quantum_segmentation`` - Quantum image segmentation

**Quantum Machine Learning**
- ``quscope.qml.image_encoding`` - ML-focused quantum image encoding
- Support for various encoding schemes optimized for ML workflows

**EELS Analysis**
- ``quscope.eels_analysis.preprocessing`` - EELS data preprocessing
- ``quscope.eels_analysis.quantum_processing`` - Quantum algorithms for EELS analysis

**Backend Management**
- ``quscope.quantum_backend`` - Unified interface for quantum backends
- Support for Qiskit Aer simulators and IBM Quantum hardware
- Error handling and retry mechanisms for robust execution

**Documentation & Examples**
- Comprehensive API documentation with Sphinx
- Interactive Jupyter notebooks demonstrating key features
- Complete quantum image encoding validation examples
- Step-by-step tutorials for common use cases

**Package Infrastructure**
- PyPI-ready package structure with proper metadata
- Read the Docs integration for online documentation
- Comprehensive test suite with pytest
- Development dependencies and linting configuration

Dependencies
------------
- Python >= 3.9
- qiskit >= 0.45.0
- qiskit-aer >= 0.13.0  
- numpy >= 1.21.0
- pillow >= 8.0.0
- scipy >= 1.7.0

Optional Dependencies
-------------------------
- matplotlib >= 3.5.0 (visualization)
- jupyter >= 1.0.0 (notebook examples)
- pandas >= 1.3.0 (data analysis)

Known Issues
------------
- Large quantum circuits (>20 qubits) may have slow simulation times
- Some advanced quantum hardware features require additional setup

Future Plans
------------
- Enhanced quantum ML algorithms
- Real-time microscopy data processing
- Integration with more quantum hardware backends
- Performance optimizations for large-scale image processing
