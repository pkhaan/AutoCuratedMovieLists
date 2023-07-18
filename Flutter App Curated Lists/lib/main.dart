import 'package:flutter/material.dart'
    show
        BuildContext,
        MaterialApp,
        StatelessWidget,
        TargetPlatform,
        ThemeData,
        Widget,
        runApp;
import 'package:sizer/sizer.dart';
import 'utils/constants.dart';
import 'screens/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart' show kIsWeb;

// void main() {
//   runApp(MyApp());
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Sizer(
//       builder: (context, orientation, deviceType) {
//         return MaterialApp(
//           debugShowCheckedModeBanner: false,
//           title: 'Auto Curated Movie Lists',
//           theme: ThemeData.dark().copyWith(
//             platform: TargetPlatform.android,
//             primaryColor: kPrimaryColor,
//             scaffoldBackgroundColor: kPrimaryColor,
//           ),
//           home: HomeScreen(
//             key: kHomeScreenKey,
//           ),
//         );
//       },
//     );
//   }
// }

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Sizer(
      builder: (context, orientation, deviceType) {
        ThemeData themeData;

        // Customize the theme for the web platform
        if (kIsWeb) {
          themeData = ThemeData.dark().copyWith(
            primaryColor: const Color.fromARGB(
                255, 33, 243, 75), // Customize the primary color for the web
            scaffoldBackgroundColor:
                Colors.white, // Customize the background color for the web
            // Add more customizations as needed
          );
        } else {
          // Use the default theme for Android and iOS
          themeData = ThemeData.dark().copyWith(
            platform: TargetPlatform.android,
            primaryColor: kPrimaryColor,
            scaffoldBackgroundColor: kPrimaryColor,
          );
        }

        return MaterialApp(
          debugShowCheckedModeBanner: false,
          title: 'Auto Curated Movie Lists',
          theme: themeData,
          home: HomeScreen(
            key: kHomeScreenKey,
          ),
        );
      },
    );
  }
}
