//This is an example code for the camera//
import React from 'react';
import {createStackNavigator, createAppContainer} from 'react-navigation';
import HomeScreen from './screens/HomeScreen';
import CameraScreen from './screens/CameraScreen';

const MainNavigator = createStackNavigator({
  Home: {screen: HomeScreen},
  Camera: {screen: CameraScreen},
});

const App = createAppContainer(MainNavigator);

export default App;