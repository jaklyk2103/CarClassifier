import React from 'react';
import {
  StyleSheet,
  Alert,
  PermissionsAndroid,
  Platform,
} from 'react-native';
import { CameraKitCameraScreen } from 'react-native-camera-kit';
 
export default class CameraScreen extends React.Component {
    state = { 
        userWantsToExitCamera: false 
    };
  constructor(props) {
    super(props);
  }

  onPress() {
    var that = this;
    if (Platform.OS === 'android') {
      async function requestCameraPermission() {
        try {
          const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.CAMERA,
            {
              title: 'CameraExample App Camera Permission',
              message: 'CameraExample App needs access to your camera ',
            }
          );
          if (granted === PermissionsAndroid.RESULTS.GRANTED) {
            //If CAMERA Permission is granted
            //Calling the WRITE_EXTERNAL_STORAGE permission function
            requestExternalWritePermission();
          } else {
            alert('CAMERA permission denied');
          }
        } catch (err) {
          alert('Camera permission err', err);
          console.warn(err);
        }
      }
      async function requestExternalWritePermission() {
        try {
          const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.WRITE_EXTERNAL_STORAGE,
            {
              title: 'CameraExample App External Storage Write Permission',
              message:
                'CameraExample App needs access to Storage data in your SD Card ',
            }
          );
          if (granted === PermissionsAndroid.RESULTS.GRANTED) {
            //If WRITE_EXTERNAL_STORAGE Permission is granted
            //Calling the READ_EXTERNAL_STORAGE permission function
            requestExternalReadPermission();
          } else {
            alert('WRITE_EXTERNAL_STORAGE permission denied');
          }
        } catch (err) {
          alert('Write permission err', err);
          console.warn(err);
        }
      }
      async function requestExternalReadPermission() {
        try {
          const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.READ_EXTERNAL_STORAGE,
            {
              title: 'CameraExample App Read Storage Read Permission',
              message: 'CameraExample App needs access to your SD Card ',
            }
          );
          if (granted === PermissionsAndroid.RESULTS.GRANTED) {
            //If READ_EXTERNAL_STORAGE Permission is granted
            //changing the state to re-render and open the camera
            //in place of activity indicator
            that.setState({ isPermitted: true });
          } else {
            alert('READ_EXTERNAL_STORAGE permission denied');
          }
        } catch (err) {
          alert('Read permission err', err);
          console.warn(err);
        }
      }
      //Calling the camera permission function
      requestCameraPermission();
    } else {
      this.setState({ isPermitted: true });
    }
  }

  onBottomButtonPressed(event) {
    const captureImages = JSON.stringify(event.captureImages);
    if (event.type === 'left') {
      const {navigate} = this.props.navigation;
      navigate('Home', {});
    } else {
      Alert.alert(
        event.type,
        captureImages,
        [{ text: 'OK', onPress: () => console.log('OK Pressed') }],
        { cancelable: false }
      );
    }
  }

    render() {
        return (
        <CameraKitCameraScreen
            // Buttons to perform action done and cancel
            actions={{ rightButtonText: 'Done', leftButtonText: 'Cancel' }}
            onBottomButtonPressed={event => this.onBottomButtonPressed(event)}
            flashImages={{
            // Flash button images
            on: require('../assets/flashon.png'),
            off: require('../assets/flashoff.png'),
            auto: require('../assets/flashauto.png'),
            }}
            cameraFlipImage={require('../assets/flip.png')}
            captureButtonImage={require('../assets/capture.png')}
        />
        );
    }
}