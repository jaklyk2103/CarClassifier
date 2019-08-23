import React from 'react';
import {
  Text,
  View,
} from 'react-native';

import LoadingAnimation from './../components/loadingAnimation';
 
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
          <LoadingAnimation show={true}></LoadingAnimation>
        </View>
      );
  }
}