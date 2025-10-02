# BlueQubit Python SDK

## Quick Start

1. Register on https://app.bluequbit.io and copy the API token.

2. Install Python SDK from PyPI:
```
    pip install bluequbit
```

3. Import and initialize the SDK (importing also Qiskit for circuit building):

```
    import qiskit

    import bluequbit

    bq_client = bluequbit.init("<token>")
```

4. An example of how to run a Qiskit circuit using the SDK:

```
    qc_qiskit = qiskit.QuantumCircuit(2)
    qc_qiskit.h(0)
    qc_qiskit.x(1)

    job_result = bq_client.run(qc_qiskit, job_name="testing_1")

    state_vector = job_result.get_statevector() 
    # returns a NumPy array of [0. +0.j 0. +0.j 0.70710677+0.j 0.70710677+0.j]
```

5. Here is an example to run the previous code asynchronously:

```
    # This line is non-blocking.
    job = bq_client.run(qc_qiskit, job_name="testing_1", asynchronous=True)

    # This line blocks until the job is completed.
    job_result = bq_client.wait(job.job_id)

    # If you want to cancel a pending job.
    bq_client.cancel(job.job_id)
```

6. This is how you can use our `mps.cpu` device:

```
    # a 40 qubit GHZ state
    num_qubits = 40
    qc = qiskit.QuantumCircuit(num_qubits)
    qc.h(0)
    for i in range(num_qubits - 1):
        qc.cx(i, i+1)
    
    qc.measure_all()
    
    options = {
        "mps_bond_dimension": 2,
    }
    result = bq_client.run(qc, device="mps.cpu", options=options) # should take ~30seconds
    print(result.get_counts())
```   

The `mps.gpu` device can be used in the same way. 
Note that while `mps.gpu` is faster, you need to have a certain amount of minimal balance to be able to use it.

7. An example of how to use our Pauli Path Simulator to compute observable expectations:

```
    qc = qiskit.QuantumCircuit(3)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.ry(0.3, 0)
    qc.rz(0.6, 1)
    qc.rx(0.7, 2)

    # observable
    pauli_sum = [
        ("XYZ", -0.5),
        ("XXX", 0.2),
        ("XII", 0.3),
        ("III", 0.4),
    ]

    options = {
        "pauli_path_truncation_threshold": 0.1,
    }
    result = bq_client.run(qc, device="pauli-path", pauli_sum=pauli_sum, options=options)
    expectation_value = result.expectation_value
    # returns 0.9411262759533625
```    

8. An example of how to run a Pennylane circuit:

```
    import pennylane as qml
    from pennylane import numpy as np
    
    dev = qml.device('bluequbit.cpu', wires=1, token="<token>")
    
    @qml.qnode(dev)
    def circuit(angle):
        qml.RY(angle, wires=0)
        return qml.probs(wires=0)
    
    
    probabilities = circuit(np.pi / 4)
    # returns a NumPy array of [0.85355339 0.14644661]
```
To use the Pennylane plugin, you must have `pennylane` version 0.39 or above installed. 
    

9. This SDK requires Python versions 3.9 or above. But we recommend using Python 3.10 or above.
The package is tested extensively on Python 3.10.

## Full reference

Please find detailed reference at https://app.bluequbit.io/sdk-docs.

## Questions and Issues

Please submit questions and issues to info@bluequbit.io.
