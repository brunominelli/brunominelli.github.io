import 'package:flutter/material.dart';
import 'package:portfolio/views/home_view.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.transparent,
            primary: Colors.transparent,
            secondary: Colors.transparent,
            tertiary: Colors.transparent,
            background: Colors.transparent,
            surface: Colors.transparent,
          ),
          textTheme: TextTheme()),
      home: const HomeView(),
    );
  }
}
