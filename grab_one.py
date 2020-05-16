from pypylon import pylon, genicam

tlFactory = pylon.TlFactory.GetInstance()
devices = tlFactory.EnumerateDevices()
cameraArray = pylon.InstantCameraArray(len(devices))

for i, camera in enumerate(cameraArray):
    camera.Attach(tlFactory.CreateDevice(devices[i].GetFullName()))
    camera.Open()
    camera.RegisterConfiguration(pylon.SoftwareTriggerConfiguration(), pylon.RegistrationMode_ReplaceAll,
                             pylon.Cleanup_Delete)
    
    pylon.FeaturePersistence.Load(nodeFile, camera.GetNodeMap(), True)
    # camera[i].TriggerSelector = "FrameBurstStart" # <== Selector first!
    # camera[i].TriggerSource = "Line3"
    # camera[i].TriggerMode = 'On'

    # camera[i].LineSelector = "Line3"
    # camera[i].LineMode = "Input"

    # camera.Open()

    camera.StartGrabbing(pylon.GrabStrategy_OneByOne, pylon.GrabLoop_ProvidedByInstantCamera)

    print(camera.GetDeviceInfo())
    print(camera.ExposureTime.camera.GetValue())

camera.WaitForFrameTriggerReady(1000)