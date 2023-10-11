import 'package:flutter/material.dart';
import 'package:portfolio/widgets/content_card_widget.dart';
import 'package:portfolio/widgets/header_widget.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  final PageController controller = PageController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: HeaderWidget(controller: controller),
      body:
          /* PageView(
          //   controller: controller,
          //   scrollDirection: Axis.vertical,
          //   physics: const NeverScrollableScrollPhysics(),*/
          SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                SizedBox(
                  width: MediaQuery.of(context).size.width * 0.40,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: <Widget>[
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(
                          'Olá,',
                          style: Theme.of(context)
                              .textTheme
                              .titleLarge
                              ?.copyWith(
                                color: Theme.of(context).colorScheme.primary,
                              ),
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(
                          'EU SOU\nBRUNO MINELLI',
                          style: Theme.of(context)
                              .textTheme
                              .displayMedium
                              ?.copyWith(
                                color: Theme.of(context).colorScheme.primary,
                                fontWeight: FontWeight.bold,
                              ),
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(
                          'Seja bem-vindo!',
                          style: Theme.of(context)
                              .textTheme
                              .titleLarge
                              ?.copyWith(
                                color: Theme.of(context).colorScheme.primary,
                              ),
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(
                  width: MediaQuery.of(context).size.width * 0.40,
                  child: Image.asset('assets/image_bruno_minelli.png'),
                ),
              ],
            ),
            Column(
              children: <Widget>[
                Image.asset('assets/logo_bruno_minelli.png'),
                Text(
                  'Bruno Minelli',
                  style: Theme.of(context).textTheme.displayMedium?.copyWith(
                        color: Theme.of(context).colorScheme.primary,
                        fontWeight: FontWeight.bold,
                      ),
                ),
                Text(
                  'Desenvolvedor de Software | Consultor | '
                  'Entusiasta de Jogos e Tecnologia',
                  style: Theme.of(context).textTheme.titleLarge?.copyWith(
                        color: Theme.of(context).colorScheme.primary,
                      ),
                ),
                SizedBox(
                  width: MediaQuery.of(context).size.width * 0.80,
                  child: Row(
                    children: <Widget>[
                      Expanded(
                        child: Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: ContentCardWidget(
                            icon: Icons.gamepad_rounded,
                            content:
                                'Sou apaixonado por jogos e tecnologia com '
                                'mais de dez anos de experiência no setor de '
                                'Tecnologia da Informação.',
                            backgroundColor:
                                Theme.of(context).colorScheme.tertiary,
                            contentColor:
                                Theme.of(context).colorScheme.secondary,
                          ),
                        ),
                      ),
                      Expanded(
                        child: Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: ContentCardWidget(
                            icon: Icons.devices_rounded,
                            content:
                                'Atuo com desenvolvimento de sistemas web e '
                                'mobile e minha comunicação assertiva me permite '
                                'alinhar expectativas e superar desafios.',
                            backgroundColor:
                                Theme.of(context).colorScheme.secondary,
                            contentColor:
                                Theme.of(context).colorScheme.tertiary,
                            topIcon: true,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}
