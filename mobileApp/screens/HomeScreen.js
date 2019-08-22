import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  PermissionsAndroid,
  Platform,
  TouchableOpacity,
} from 'react-native';
 
export default class HomeScreen extends React.Component {

  constructor(props) {
    super(props);
    this.handleTakePhotoClick = this.handleTakePhotoClick.bind(this);
    this.requestCameraPermission = this.requestCameraPermission.bind(this);
    this.requestExternalReadPermission = this.requestExternalReadPermission.bind(this);
    this.requestExternalWritePermission = this.requestExternalWritePermission.bind(this);
  }

  async requestCameraPermission() {
    try {
      const permissionResult = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.CAMERA,
        {
          title: 'CarClassifier App Camera Permission',
          message: 'CarClassifier App needs access to your camera',
        }
      );
      if (permissionResult === PermissionsAndroid.RESULTS.GRANTED) {
        return await this.requestExternalWritePermission().then((permission) => {
          return (permission) ? true : false;
        });
      } else {
        alert('Camera permission denied, application cannot use camera.');
      }
    } catch (err) {
      alert('Camera permission err', err);
      console.warn(err);
    }
  }

  async requestExternalWritePermission() {
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
        return await this.requestExternalReadPermission().then((permission) => {
          return (permission) ? true : false;
        });
      } else {
        alert('WRITE_EXTERNAL_STORAGE permission denied');
      }
    } catch (err) {
      alert('Write permission err', err);
      console.warn(err);
    }
  }

  async requestExternalReadPermission() {
    try {
      const permissionResult = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.READ_EXTERNAL_STORAGE,
        {
          title: 'CarClassifier App Read Storage Read Permission',
          message: 'CarClassifier App needs access to your SD Card ',
        }
      );
      if (permissionResult === PermissionsAndroid.RESULTS.GRANTED) {
        // all permissions granted
        return true;
      } else {
        alert('READ_EXTERNAL_STORAGE permission denied');
        return false;
      }
    } catch (err) {
      alert('Read permission err', err);
      console.warn(err);
    }
  }

  handleTakePhotoClick() {
    if (Platform.OS === 'android') {
      this.requestCameraPermission()
      .then((permission) => {
        if (permission === true) {
          const {navigate} = this.props.navigation;
          navigate('Camera', {});
        }
      });
    } else {
      alert('Not an Android device. Application cannot be used.');
    }
  }

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.welcomeWrapper}>
          <Text style={styles.welcome}>
            Welcome to the Car Classifier!
          </Text>
        </View>
        <TouchableOpacity
          style={styles.button}
          onPress={this.handleTakePhotoClick}>
          <Text style={styles.buttonText}>TAKE PHOTO OF A CAR</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFB74D',
  },
  welcomeWrapper: {
    justifyContent: 'flex-start',
    marginBottom: 350
  },
  welcome: {
    textAlign: 'center',
    fontSize: 35,
    fontWeight: 'bold',
  },
  button: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#EEEEEE',
    width: 300,
    height: 50,
  },
  buttonText: {
    fontSize: 14,
    fontWeight: '900',
  }
});