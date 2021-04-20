import h5py

hf = h5py.File('cnn_model_keras2.h5')

for i in hf.attrs:
    print(i)
print(hf.attrs['keras_version'])