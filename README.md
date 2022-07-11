## Require
Python version >= 3.7

*This document uses Python3.7 as an example*

## Essential Install
```
apt-get install python3-venv
apt-get install python3.7-dev
```

## Install Dependent
```
python3.7 -m venv venv
source venv/bin/activate

pip install wheel
pip install grpcio
pip install protobuf
pip install grpcio-tools
```

## Generate Kaspa gRPC client 
```
cd proto

python -m grpc_tools.protoc -I. --python_out=./client --grpc_python_out=./client ./message.proto
python -m grpc_tools.protoc -I. --python_out=./client --grpc_python_out=./client ./rpc.proto
```

## Install 
```
python setup.py install
```

## Test
```
python test_import.py
```



