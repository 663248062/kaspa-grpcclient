## Require
Python version >= 3.7

*This document uses Python3.7 as an example*

## Essential Install
```
apt-get install python3-venv
apt-get install python3.7-dev
```

## Install Dependent (virtual environment)
```
python3.7 -m venv venv
source venv/bin/activate

pip install wheel
pip install grpcio
pip install protobuf
pip install grpcio-tools
```

## Generate Kaspa gRPC client (virtual environment)
```
python -m grpc_tools.protoc -I. --python_out=./kaspa_grpcclient --grpc_python_out=./kaspa-grpcclient ./proto/rpc.proto
python -m grpc_tools.protoc -I. --python_out=./kaspa_grpcclient --grpc_python_out=./kaspa-grpcclient ./proto/message.proto

touch ./kaspa-grpcclient/proto/__init__.py
```

## Install 
```
python setup.py install
```

## Test
```
python test_import.py
```



