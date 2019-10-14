# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FibonacciApp(models.Model):
	latency = models.CharField(max_length=100, blank=True, null=True)
	numeric = models.PositiveIntegerField(blank=True, null=True)
	output = models.PositiveIntegerField(blank=True, null=True)
	
	def __str__(self):
		return self.output

	
        