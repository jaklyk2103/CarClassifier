import React from 'react';
import {
  StyleSheet,
  Alert,
  PermissionsAndroid,
  Platform,
} from 'react-native';
import { CameraKitCameraScreen } from 'react-native-camera-kit';
 
export default class CameraScreen extends React.Component {
  constructor(props) {
    super(props);
  }

  onPress() {
    if (Platform.OS === 'android') {
      async function requestCameraPermission() {
        try {
          const permissionResult = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.CAMERA,
            {
              title: 'CarClassifier App Camera Permission',
              message: 'CarClassifier App needs access to your camera',
            }
          );
          if (permissionResult === PermissionsAndroid.RESULTS.GRANTED) {
            requestExternalWritePermission();
          } else {
            alert('Camera permission denied, application cannot use camera.');
          }
        } catch (err) {
          alert('Camera permission err', err);
          console.warn(err);
        }
      }

      async function requestExternalWritePermission() {
        try {
          const permissionResult = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.WRITE_EXTERNAL_STORAGE,
            {
              title: 'CarClassifier App External Storage Write Permission',
              message:
                'CarClassifier App needs access to Storage data in your SD Card',
            }
          );
          if (permissionResult === PermissionsAndroid.RESULTS.GRANTED) {
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
          const permissionResult = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.READ_EXTERNAL_STORAGE,
            {
              title: 'CarClassifier App Read Storage Read Permission',
              message: 'CarClassifier App needs access to your SD Card',
            }
          );
          if (permissionResult === PermissionsAndroid.RESULTS.GRANTED) {
            // all permissions granted
            this.setState({ isPermitted: true });
          } else {
            alert('READ_EXTERNAL_STORAGE permission denied');
          }
        } catch (err) {
          alert('Read permission err', err);
          console.warn(err);
        }
      }

      requestCameraPermission();
    } else {
      alert('Not an Android device. Application cannot be used.');
      this.setState({ isPermitted: false });
    }
  }

  onBottomButtonPressed(event) {
    // const captureImages = JSON.stringify(event.captureImages);
    const {navigate} = this.props.navigation;
    if (event.type === 'left') {
      navigate('Home', {});
    } else if (event.type === 'right') {
      navigate('Classify', {});
    }
  }

  render() {
      return (
      <CameraKitCameraScreen
          // Buttons to perform action done and cancel
          actions={{ rightButtonText: 'Classify', leftButtonText: 'Cancel' }}
          onBottomButtonPressed={event => this.onBottomButtonPressed(event)}
          flashImages={{
          // Flash button images
          off: require('../assets/flashoff.png'),
          on: require('../assets/flashon.png'),
          auto: require('../assets/flashauto.png'),
          }}
          cameraFlipImage={require('../assets/flip.png')}
          captureButtonImage={require('../assets/camera64.png')}
      />
      );
  }
}