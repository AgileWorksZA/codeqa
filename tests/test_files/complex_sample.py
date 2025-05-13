#!/usr/bin/env python3
"""
A sample file with various levels of complexity for testing the metrics module.
"""

import os
import sys
import math
import json
import datetime
from collections import defaultdict


def very_complex_function(data, threshold=10):
    """Function with high complexity (F grade)."""
    result = {}
    processed = 0
    
    if not data:
        return None
    
    for key, values in data.items():
        result[key] = []
        
        # Skip empty collections
        if not values:
            continue
            
        # Apply different processing based on conditions
        if isinstance(values, dict):
            for sub_key, sub_value in values.items():
                if sub_value > threshold:
                    result[key].append((sub_key, sub_value * 2))
                elif sub_value < 0:
                    result[key].append((sub_key, 0))
                else:
                    result[key].append((sub_key, sub_value))
                    
        elif isinstance(values, list):
            for item in values:
                if item > threshold:
                    result[key].append(item * 2)
                elif item < 0:
                    result[key].append(0)
                else:
                    result[key].append(item)
        
        # Special case handling
        if key.startswith('special_'):
            processed += 1
            if processed > 5:
                # Complex condition
                for i in range(len(result[key])):
                    if i % 2 == 0 and i % 3 == 0:
                        result[key][i] = result[key][i] * 3
                    elif i % 2 == 0:
                        result[key][i] = result[key][i] * 2
                    elif i % 3 == 0:
                        result[key][i] = result[key][i] + 1
    
    return result


def medium_complex_function(n, factors=[2, 3, 5]):
    """Function with medium complexity (C grade)."""
    counts = defaultdict(int)
    
    for i in range(1, n+1):
        for factor in factors:
            if i % factor == 0:
                counts[factor] += 1
                
                # Special case for combinations
                if factor == 2 and i % 3 == 0:
                    counts['2_and_3'] += 1
                elif factor == 3 and i % 5 == 0:
                    counts['3_and_5'] += 1
    
    # Calculate percentages
    total = n
    percentages = {}
    for factor, count in counts.items():
        percentages[factor] = (count / total) * 100
        
    return percentages


def simple_function(x):
    """Function with low complexity (A grade)."""
    return x * 2


class ComplexityTestClass:
    """Class with methods of varying complexity."""
    
    def __init__(self, value):
        """Simple initialization method (A grade)."""
        self.value = value
        self.data = {}
    
    def complex_method(self, items, threshold=5):
        """Method with high complexity (D grade)."""
        results = []
        counts = {
            'above': 0,
            'below': 0,
            'equal': 0
        }
        
        for i, item in enumerate(items):
            # Apply different processing based on position and value
            if i % 2 == 0:
                if item > threshold:
                    results.append(item * 2)
                    counts['above'] += 1
                elif item < threshold:
                    results.append(item / 2)
                    counts['below'] += 1
                else:
                    results.append(item)
                    counts['equal'] += 1
            else:
                if item > threshold * 2:
                    results.append(item - threshold)
                    counts['above'] += 1
                elif item < threshold / 2:
                    results.append(item + threshold)
                    counts['below'] += 1
                else:
                    # Special case for items in the middle range
                    if self.value > item:
                        results.append(item + self.value)
                    else:
                        results.append(item - self.value)
                    counts['equal'] += 1
        
        # Post-processing
        if counts['above'] > counts['below'] * 2:
            for i in range(len(results)):
                if i % 3 == 0:
                    results[i] = results[i] * 0.8
        elif counts['below'] > counts['above']:
            for i in range(len(results)):
                if i % 2 == 0:
                    results[i] = results[i] * 1.2
                    
        self.data['last_results'] = results
        self.data['last_counts'] = counts
        
        return results, counts
    
    def simple_method(self, x, y):
        """Method with low complexity (A grade)."""
        return x + y
    
    def medium_method(self, data):
        """Method with medium complexity (B grade)."""
        result = {}
        if not data:
            return None
            
        for key, value in data.items():
            if isinstance(value, list):
                result[key] = sum(value)
            elif isinstance(value, dict):
                result[key] = len(value)
            else:
                result[key] = value
                
        return result