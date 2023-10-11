import 'package:flutter/material.dart';

class HeaderWidget extends StatelessWidget implements PreferredSizeWidget {
  HeaderWidget({super.key, required this.controller});

  final PageController controller;

  final List<String> actions = [
    'home',
    'sobre',
    'experiência profissional',
    'serviços',
    'fale comigo',
  ];

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Theme.of(context).colorScheme.background,
      foregroundColor: Theme.of(context).colorScheme.background,
      surfaceTintColor: Theme.of(context).colorScheme.background,
      title: Row(
        children: [
          Image.asset('assets/logo_bruno_minelli.png'),
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 16.0),
            child: Text('Bruno Minelli'),
          ),
        ],
      ),
      titleTextStyle: Theme.of(context).textTheme.displayMedium?.copyWith(
            fontWeight: FontWeight.w900,
            color: Theme.of(context).colorScheme.primary,
          ),
      actions: List.generate(
        actions.length,
        (index) => Padding(
          padding: const EdgeInsets.symmetric(horizontal: 8.0),
          child: TextButton(
            onPressed: () => controller.animateToPage(index,
                duration: const Duration(seconds: 1),
                curve: Curves.fastOutSlowIn),
            child: Text(actions[index]),
          ),
        ),
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kTextTabBarHeight);
}
