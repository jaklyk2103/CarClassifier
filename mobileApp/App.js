import {createStackNavigator, createAppContainer} from 'react-navigation';
import HomeScreen from './screens/HomeScreen';
import CameraScreen from './screens/CameraScreen';
import ClassifyScreen from './screens/ClassifyScreen';

const MainNavigator = createStackNavigator({
  Home: {
    screen: HomeScreen,
    navigationOptions: {
      title: 'Welcome',
      header: null
    }},
  Camera: {screen: CameraScreen,
    navigationOptions: {
      title: 'Camera',
      header: null
    }},  
  Classify: {screen: ClassifyScreen,
    navigationOptions: {
      title: 'Classify',
      header: null
    }},  
});

const App = createAppContainer(MainNavigator);

export default App;