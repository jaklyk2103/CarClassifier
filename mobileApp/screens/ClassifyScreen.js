import React from 'react';
import {
  Alert,
  PermissionsAndroid,
  Platform,
} from 'react-native';
 
export default class ClassifyScreen extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
      return (
        <View>
          <Text>
            Classifying given image here... To be done.
          </Text>
        </View>
      );
  }
}