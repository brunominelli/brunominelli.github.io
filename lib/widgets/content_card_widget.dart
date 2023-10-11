import 'package:flutter/material.dart';

class ContentCardWidget extends StatelessWidget {
  const ContentCardWidget({
    super.key,
    required this.content,
    this.icon,
    required this.contentColor,
    required this.backgroundColor,
    this.topIcon = false,
  });

  final IconData? icon;
  final String content;
  final Color contentColor;
  final Color backgroundColor;
  final bool topIcon;

  @override
  Widget build(BuildContext context) {
    return topIcon
        ? Column(
            children: <Widget>[
              Visibility(
                visible: icon != null,
                child: Icon(icon, size: 100),
              ),
              Container(
                padding: const EdgeInsets.all(52),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16.0),
                  color: backgroundColor,
                ),
                child: Text(
                  content,
                  style: Theme.of(context)
                      .textTheme
                      .titleLarge
                      ?.copyWith(color: contentColor),
                ),
              ),
            ],
          )
        : Column(
            children: <Widget>[
              Container(
                padding: const EdgeInsets.all(52),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16.0),
                  color: backgroundColor,
                ),
                child: Text(
                  content,
                  style: Theme.of(context)
                      .textTheme
                      .titleLarge
                      ?.copyWith(color: contentColor),
                ),
              ),
              Visibility(
                visible: icon != null,
                child: Icon(icon, size: 100),
              ),
            ],
          );
  }
}
