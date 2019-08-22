import React from 'react';
import { CameraKitCameraScreen } from 'react-native-camera-kit';
 
export default class CameraScreen extends React.Component {
  constructor(props) {
    super(props);
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
          actions={{ rightButtonText: 'Classify', leftButtonText: 'Cancel' }}
          onBottomButtonPressed={event => this.onBottomButtonPressed(event)}
          flashImages={{
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