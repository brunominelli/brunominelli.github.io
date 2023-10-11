import 'package:flutter/material.dart';
import 'package:portfolio/routes/app_routes.dart';
import 'package:google_fonts/google_fonts.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color.fromRGBO(88, 68, 100, 1),
          primary: const Color.fromRGBO(88, 68, 100, 1),
          secondary: const Color.fromRGBO(52, 38, 56, 1),
          tertiary: const Color.fromRGBO(245, 240, 250, 1),
          background: const Color.fromRGBO(254, 251, 251, 1),
          surface: const Color.fromRGBO(20, 20, 20, 1),
        ),
        textTheme: GoogleFonts.robotoTextTheme(),
      ),
      routes: routes,
      debugShowCheckedModeBanner: false,
    );
  }
}
