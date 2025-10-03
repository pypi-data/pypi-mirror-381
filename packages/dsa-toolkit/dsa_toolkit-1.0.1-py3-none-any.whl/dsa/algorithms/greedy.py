"""
greedy.py - DSA Toolkit

This module implements classic greedy algorithms:
- Activity Selection Problem
- Fractional Knapsack
- Job Scheduling with Deadlines
- Huffman Coding
- Minimum Coin Change
- Gas Station Problem
- Meeting Rooms
- Container With Most Water

Features:
- Comprehensive greedy algorithm implementations
- Step-by-step debug tracing
- Real-world problem examples
- Optimal and approximation algorithms
"""

from typing import List, Tuple, Dict, Optional, Any
import heapq
from collections import defaultdict, Counter


# ============================================================================
# ACTIVITY SELECTION PROBLEM
# ============================================================================

def activity_selection(activities: List[Tuple[int, int]], debug: bool = False) -> List[int]:
    """
    Activity Selection Problem: Select maximum number of non-overlapping activities.
    
    Args:
        activities: List of (start_time, end_time) tuples
        debug: Enable debug output
    
    Returns:
        List of selected activity indices
    """
    if not activities:
        return []
    
    # Sort by end time
    indexed_activities = [(end, start, i) for i, (start, end) in enumerate(activities)]
    indexed_activities.sort()
    
    selected = [indexed_activities[0][2]]  # Select first activity
    last_end = indexed_activities[0][0]
    
    if debug:
        print(f"Activity Selection (sorted by end time):")
        print(f"Activities: {[(start, end) for end, start, _ in indexed_activities]}")
        print(f"Selected activity {indexed_activities[0][2]}: ({indexed_activities[0][1]}, {indexed_activities[0][0]})")
    
    for end, start, idx in indexed_activities[1:]:
        if start >= last_end:  # No overlap
            selected.append(idx)
            last_end = end
            if debug:
                print(f"Selected activity {idx}: ({start}, {end})")
        elif debug:
            print(f"Skipped activity {idx}: ({start}, {end}) - overlaps with previous")
    
    if debug:
        print(f"Total selected activities: {len(selected)}")
    
    return selected


# ============================================================================
# FRACTIONAL KNAPSACK
# ============================================================================

def fractional_knapsack(items: List[Tuple[int, int]], capacity: int, debug: bool = False) -> Tuple[float, List[Tuple[int, float]]]:
    """
    Fractional Knapsack: Maximize value with given weight capacity.
    
    Args:
        items: List of (value, weight) tuples
        capacity: Maximum weight capacity
        debug: Enable debug output
    
    Returns:
        Tuple of (max_value, selected_items_with_fractions)
    """
    if not items or capacity <= 0:
        return 0.0, []
    
    # Calculate value-to-weight ratio and sort by it (descending)
    indexed_items = [(value/weight, value, weight, i) for i, (value, weight) in enumerate(items)]
    indexed_items.sort(reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    selected = []
    
    if debug:
        print(f"Fractional Knapsack (capacity: {capacity}):")
        print(f"Items sorted by value/weight ratio:")
        for ratio, value, weight, idx in indexed_items:
            print(f"  Item {idx}: value={value}, weight={weight}, ratio={ratio:.2f}")
    
    for ratio, value, weight, idx in indexed_items:
        if remaining_capacity >= weight:
            # Take the entire item
            selected.append((idx, 1.0))
            total_value += value
            remaining_capacity -= weight
            if debug:
                print(f"Took full item {idx}: +{value} value, {remaining_capacity} capacity left")
        elif remaining_capacity > 0:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            selected.append((idx, fraction))
            total_value += value * fraction
            if debug:
                print(f"Took {fraction:.2f} of item {idx}: +{value * fraction:.2f} value")
            remaining_capacity = 0
            break
        else:
            break
    
    if debug:
        print(f"Total value: {total_value:.2f}")
    
    return total_value, selected


# ============================================================================
# JOB SCHEDULING WITH DEADLINES
# ============================================================================

def job_scheduling_deadlines(jobs: List[Tuple[str, int, int]], debug: bool = False) -> Tuple[List[str], int]:
    """
    Job Scheduling with Deadlines: Maximize profit within deadlines.
    
    Args:
        jobs: List of (job_id, deadline, profit) tuples
        debug: Enable debug output
    
    Returns:
        Tuple of (scheduled_jobs, total_profit)
    """
    if not jobs:
        return [], 0
    
    # Sort jobs by profit (descending)
    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    
    # Initialize schedule slots
    schedule = [None] * max_deadline
    scheduled_jobs = []
    total_profit = 0
    
    if debug:
        print(f"Job Scheduling with Deadlines:")
        print(f"Jobs sorted by profit: {jobs_sorted}")
        print(f"Available time slots: {max_deadline}")
    
    for job_id, deadline, profit in jobs_sorted:
        # Find the latest available slot before deadline
        for slot in range(min(deadline - 1, max_deadline - 1), -1, -1):
            if schedule[slot] is None:
                schedule[slot] = job_id
                scheduled_jobs.append(job_id)
                total_profit += profit
                if debug:
                    print(f"Scheduled job {job_id} in slot {slot + 1}: +{profit} profit")
                break
        else:
            if debug:
                print(f"Could not schedule job {job_id} (deadline: {deadline}, profit: {profit})")
    
    if debug:
        print(f"Final schedule: {[job if job else 'FREE' for job in schedule]}")
        print(f"Total profit: {total_profit}")
    
    return scheduled_jobs, total_profit


# ============================================================================
# HUFFMAN CODING
# ============================================================================

class HuffmanNode:
    """Node for Huffman coding tree."""
    
    def __init__(self, char: Optional[str], freq: int, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(text: str, debug: bool = False) -> Tuple[Dict[str, str], str, HuffmanNode]:
    """
    Huffman Coding: Generate optimal prefix-free encoding.
    
    Args:
        text: Input text to encode
        debug: Enable debug output
    
    Returns:
        Tuple of (character_codes, encoded_text, huffman_tree_root)
    """
    if not text:
        return {}, "", None
    
    # Count character frequencies
    freq = Counter(text)
    
    if len(freq) == 1:
        # Special case: only one unique character
        char = list(freq.keys())[0]
        return {char: '0'}, '0' * len(text), HuffmanNode(char, freq[char])
    
    # Create priority queue with leaf nodes
    heap = [HuffmanNode(char, frequency) for char, frequency in freq.items()]
    heapq.heapify(heap)
    
    if debug:
        print(f"Huffman Coding for text: '{text}'")
        print(f"Character frequencies: {dict(freq)}")
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
        
        if debug:
            left_char = left.char if left.char else f"Internal({left.freq})"
            right_char = right.char if right.char else f"Internal({right.freq})"
            print(f"Merged: {left_char} + {right_char} = Internal({merged.freq})")
    
    root = heap[0]
    
    # Generate codes
    codes = {}
    def generate_codes(node, code=""):
        if node:
            if node.char:  # Leaf node
                codes[node.char] = code if code else "0"
            else:
                generate_codes(node.left, code + "0")
                generate_codes(node.right, code + "1")
    
    generate_codes(root)
    
    # Encode text
    encoded = ''.join(codes[char] for char in text)
    
    if debug:
        print(f"Generated codes: {codes}")
        print(f"Encoded text: {encoded}")
        print(f"Original length: {len(text) * 8} bits")
        print(f"Encoded length: {len(encoded)} bits")
        print(f"Compression ratio: {len(encoded) / (len(text) * 8):.2f}")
    
    return codes, encoded, root


def huffman_decode(encoded_text: str, root: HuffmanNode, debug: bool = False) -> str:
    """Decode Huffman encoded text."""
    if not encoded_text or not root:
        return ""
    
    decoded = []
    current = root
    
    for bit in encoded_text:
        if root.char:  # Single character case
            decoded.append(root.char)
            continue
            
        current = current.left if bit == '0' else current.right
        
        if current.char:  # Reached leaf
            decoded.append(current.char)
            current = root
            if debug:
                print(f"Decoded character: {decoded[-1]}")
    
    result = ''.join(decoded)
    if debug:
        print(f"Decoded text: '{result}'")
    
    return result


# ============================================================================
# MINIMUM COIN CHANGE (GREEDY - WORKS FOR CANONICAL SYSTEMS)
# ============================================================================

def coin_change_greedy(amount: int, coins: List[int], debug: bool = False) -> Tuple[List[int], int]:
    """
    Greedy Coin Change: Find minimum coins for given amount.
    Note: Works optimally only for canonical coin systems (like US coins).
    
    Args:
        amount: Target amount
        coins: Available coin denominations (sorted descending)
        debug: Enable debug output
    
    Returns:
        Tuple of (coins_used, total_coins)
    """
    if amount <= 0:
        return [], 0
    
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    
    if debug:
        print(f"Coin Change (Greedy) for amount: {amount}")
        print(f"Available coins: {coins_sorted}")
    
    for coin in coins_sorted:
        count = remaining // coin
        if count > 0:
            result.extend([coin] * count)
            remaining -= coin * count
            if debug:
                print(f"Used {count} coins of {coin}: remaining = {remaining}")
        
        if remaining == 0:
            break
    
    if remaining > 0:
        if debug:
            print(f"Cannot make exact change! Remaining: {remaining}")
        return [], -1  # Cannot make exact change
    
    if debug:
        print(f"Total coins used: {len(result)}")
        print(f"Coins: {result}")
    
    return result, len(result)


# ============================================================================
# GAS STATION PROBLEM
# ============================================================================

def gas_station(gas: List[int], cost: List[int], debug: bool = False) -> int:
    """
    Gas Station Problem: Find starting station to complete circular route.
    
    Args:
        gas: Gas available at each station
        cost: Gas cost to reach next station
        debug: Enable debug output
    
    Returns:
        Starting station index, or -1 if impossible
    """
    if not gas or len(gas) != len(cost):
        return -1
    
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    if total_gas < total_cost:
        if debug:
            print(f"Impossible: total_gas ({total_gas}) < total_cost ({total_cost})")
        return -1
    
    current_gas = 0
    start = 0
    
    if debug:
        print(f"Gas Station Problem:")
        print(f"Gas:  {gas}")
        print(f"Cost: {cost}")
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        
        if debug:
            print(f"Station {i}: gas={gas[i]}, cost={cost[i]}, current_gas={current_gas}")
        
        if current_gas < 0:
            start = i + 1
            current_gas = 0
            if debug:
                print(f"Reset start to station {start}")
    
    if debug:
        print(f"Starting station: {start}")
    
    return start


# ============================================================================
# MEETING ROOMS
# ============================================================================

def max_meetings(meetings: List[Tuple[int, int]], debug: bool = False) -> List[int]:
    """
    Meeting Rooms: Schedule maximum number of non-overlapping meetings.
    
    Args:
        meetings: List of (start_time, end_time) tuples
        debug: Enable debug output
    
    Returns:
        List of selected meeting indices
    """
    if not meetings:
        return []
    
    # Sort by end time
    indexed_meetings = [(end, start, i) for i, (start, end) in enumerate(meetings)]
    indexed_meetings.sort()
    
    selected = [indexed_meetings[0][2]]
    last_end = indexed_meetings[0][0]
    
    if debug:
        print(f"Meeting Room Scheduling:")
        print(f"Meetings sorted by end time:")
        for end, start, idx in indexed_meetings:
            print(f"  Meeting {idx}: ({start}, {end})")
        print(f"Selected meeting {indexed_meetings[0][2]}: ({indexed_meetings[0][1]}, {indexed_meetings[0][0]})")
    
    for end, start, idx in indexed_meetings[1:]:
        if start >= last_end:
            selected.append(idx)
            last_end = end
            if debug:
                print(f"Selected meeting {idx}: ({start}, {end})")
        elif debug:
            print(f"Skipped meeting {idx}: ({start}, {end}) - conflicts")
    
    if debug:
        print(f"Total meetings scheduled: {len(selected)}")
    
    return selected


# ============================================================================
# CONTAINER WITH MOST WATER
# ============================================================================

def container_most_water(heights: List[int], debug: bool = False) -> Tuple[int, int, int]:
    """
    Container With Most Water: Find two lines that form container with most water.
    
    Args:
        heights: Heights of vertical lines
        debug: Enable debug output
    
    Returns:
        Tuple of (max_area, left_index, right_index)
    """
    if len(heights) < 2:
        return 0, 0, 0
    
    left = 0
    right = len(heights) - 1
    max_area = 0
    best_left = 0
    best_right = 0
    
    if debug:
        print(f"Container With Most Water:")
        print(f"Heights: {heights}")
    
    while left < right:
        # Calculate area
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        
        if debug:
            print(f"Left: {left}({heights[left]}), Right: {right}({heights[right]}), Area: {area}")
        
        if area > max_area:
            max_area = area
            best_left = left
            best_right = right
            if debug:
                print(f"New max area: {max_area}")
        
        # Move the pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    if debug:
        print(f"Maximum area: {max_area} (between indices {best_left} and {best_right})")
    
    return max_area, best_left, best_right


# ============================================================================
# MINIMUM PLATFORMS NEEDED
# ============================================================================

def min_platforms(arrivals: List[int], departures: List[int], debug: bool = False) -> int:
    """
    Minimum Platforms: Find minimum platforms needed for train schedule.
    
    Args:
        arrivals: Train arrival times
        departures: Train departure times
        debug: Enable debug output
    
    Returns:
        Minimum number of platforms required
    """
    if len(arrivals) != len(departures):
        raise ValueError("Arrivals and departures must have same length")
    
    # Sort arrival and departure times
    arr_sorted = sorted(arrivals)
    dep_sorted = sorted(departures)
    
    platforms = 0
    max_platforms = 0
    i = j = 0
    
    if debug:
        print(f"Minimum Platforms Problem:")
        print(f"Arrivals:   {arr_sorted}")
        print(f"Departures: {dep_sorted}")
    
    while i < len(arr_sorted) and j < len(dep_sorted):
        if arr_sorted[i] <= dep_sorted[j]:
            platforms += 1
            i += 1
            if debug:
                print(f"Train arrives at {arr_sorted[i-1]}: platforms = {platforms}")
        else:
            platforms -= 1
            j += 1
            if debug:
                print(f"Train departs at {dep_sorted[j-1]}: platforms = {platforms}")
        
        max_platforms = max(max_platforms, platforms)
    
    if debug:
        print(f"Maximum platforms needed: {max_platforms}")
    
    return max_platforms


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Greedy Algorithms Demo")
    print("=" * 60)
    
    # 1. Activity Selection
    print("\n1. Activity Selection Problem:")
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    selected = activity_selection(activities, debug=True)
    print(f"Selected activities: {[activities[i] for i in selected]}")
    
    # 2. Fractional Knapsack
    print("\n2. Fractional Knapsack:")
    items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
    capacity = 50
    max_value, selected_items = fractional_knapsack(items, capacity, debug=True)
    
    # 3. Job Scheduling
    print("\n3. Job Scheduling with Deadlines:")
    jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    scheduled, profit = job_scheduling_deadlines(jobs, debug=True)
    
    # 4. Huffman Coding
    print("\n4. Huffman Coding:")
    text = "hello world"
    codes, encoded, root = huffman_coding(text, debug=True)
    decoded = huffman_decode(encoded, root, debug=True)
    print(f"Encoding successful: {text == decoded}")
    
    # 5. Coin Change
    print("\n5. Coin Change (Greedy):")
    amount = 93
    coins = [25, 10, 5, 1]
    coins_used, count = coin_change_greedy(amount, coins, debug=True)
    
    # 6. Gas Station
    print("\n6. Gas Station Problem:")
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    start_station = gas_station(gas, cost, debug=True)
    
    # 7. Meeting Rooms
    print("\n7. Meeting Rooms:")
    meetings = [(1, 3), (2, 4), (3, 5), (4, 6)]
    selected_meetings = max_meetings(meetings, debug=True)
    print(f"Selected meetings: {[meetings[i] for i in selected_meetings]}")
    
    # 8. Container With Most Water
    print("\n8. Container With Most Water:")
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    area, left, right = container_most_water(heights, debug=True)
    
    # 9. Minimum Platforms
    print("\n9. Minimum Platforms:")
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    min_plat = min_platforms(arrivals, departures, debug=True)
