import 'package:flutter/material.dart';
import 'package:portfolio/views/blog/blog_view.dart';
import 'package:portfolio/views/home_view.dart';
import 'package:portfolio/views/resume/resume_view.dart';

final Map<String, WidgetBuilder> routes = {
  '/': (context) => const HomeView(),
  '/blog': (context) => const BlogView(),
  '/resume': (context) => const ResumeView(),
};
