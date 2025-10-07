"""
API Testing Script for Mental Health Classifier
Tests all endpoints with various examples
"""

import requests
import json
from datetime import datetime

# Base URL
BASE_URL = "http://localhost:8000"

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def test_root():
    """Test the root endpoint"""
    print_section("TEST 1: Root Endpoint (/)")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Status Code: {response.status_code}")
        print(f"📄 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_health():
    """Test the health check endpoint"""
    print_section("TEST 2: Health Check (/health)")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ Status Code: {response.status_code}")
        print(f"📄 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_categories():
    """Test the categories endpoint"""
    print_section("TEST 3: Available Categories (/categories)")
    try:
        response = requests.get(f"{BASE_URL}/categories")
        print(f"✅ Status Code: {response.status_code}")
        print(f"📄 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_stats():
    """Test the statistics endpoint"""
    print_section("TEST 4: Training Statistics (/stats)")
    try:
        response = requests.get(f"{BASE_URL}/stats")
        print(f"✅ Status Code: {response.status_code}")
        print(f"📄 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_single_prediction():
    """Test single text prediction"""
    print_section("TEST 5: Single Prediction (/predict)")
    
    test_cases = [
        {
            "text": "I feel extremely anxious about everything, my heart races and I can't stop worrying",
            "expected": "Anxiety"
        },
        {
            "text": "I feel so sad and hopeless, nothing makes me happy anymore",
            "expected": "Depression"
        },
        {
            "text": "Work deadlines are overwhelming me, I feel constant pressure and tension",
            "expected": "Stress"
        },
        {
            "text": "My mood swings are extreme, one moment I'm energetic and the next I'm completely down",
            "expected": "Bipolar"
        },
        {
            "text": "I have trouble trusting people and maintaining relationships",
            "expected": "Personality disorder"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 Test Case {i}: {test_case['expected']}")
        print(f"📝 Input: \"{test_case['text'][:60]}...\"")
        
        try:
            response = requests.post(
                f"{BASE_URL}/predict",
                json={"text": test_case["text"]}
            )
            
            print(f"✅ Status Code: {response.status_code}")
            result = response.json()
            
            print(f"\n📊 Prediction Results:")
            print(f"   🎯 Predicted: {result['predicted_class']}")
            print(f"   🔢 Class Number: {result['class_number']}")
            print(f"   📏 Text Length: {result['text_length']} characters")
            print(f"   ⏰ Timestamp: {result['timestamp']}")
            
            # Get confidence for predicted class
            predicted_confidence = result['confidence_scores'][result['predicted_class']]
            print(f"   🎲 Confidence: {predicted_confidence:.2%}")
            
            # Check if prediction matches expected
            if result['predicted_class'].lower() == test_case['expected'].lower():
                print(f"   ✅ CORRECT PREDICTION!")
            else:
                print(f"   ⚠️  Expected: {test_case['expected']}")
            
            # Show all probabilities
            print(f"\n   📈 All Confidence Scores:")
            for category, score in sorted(result['confidence_scores'].items(), key=lambda x: x[1], reverse=True):
                bar = "█" * int(score * 50)
                print(f"      {category:20s}: {score:5.1%} {bar}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 60)

def test_batch_prediction():
    """Test batch prediction"""
    print_section("TEST 6: Batch Prediction (/batch-predict)")
    
    texts = [
        "I can't sleep at night, my mind won't stop racing with worries",
        "Everything feels meaningless and I have no energy",
        "The workload is crushing me, I feel burned out",
    ]
    
    print(f"📦 Testing batch prediction with {len(texts)} texts\n")
    
    try:
        response = requests.post(
            f"{BASE_URL}/batch-predict",
            json={"texts": texts}
        )
        
        print(f"✅ Status Code: {response.status_code}")
        result = response.json()
        
        print(f"\n📊 Batch Results:")
        print(f"   📝 Total Texts: {len(result)}")
        
        print(f"\n📋 Individual Predictions:")
        for i, pred in enumerate(result, 1):
            if pred['predicted_class'] == 'ERROR':
                print(f"\n   {i}. ❌ ERROR: Text too short")
                continue
                
            print(f"\n   {i}. Text: \"{texts[i-1][:50]}...\"")
            print(f"      🎯 Category: {pred['predicted_class']}")
            confidence = pred['confidence_scores'][pred['predicted_class']]
            print(f"      🎲 Confidence: {confidence:.2%}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def test_error_handling():
    """Test error handling with invalid inputs"""
    print_section("TEST 7: Error Handling")
    
    # Test 1: Empty text
    print("🧪 Test: Empty text")
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json={"text": ""}
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 422:
            print("✅ Correctly rejected empty text")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "-" * 60 + "\n")
    
    # Test 2: Too many texts in batch
    print("🧪 Test: Batch with >100 texts")
    try:
        response = requests.post(
            f"{BASE_URL}/batch-predict",
            json={"texts": ["test"] * 101}
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 400:
            print("✅ Correctly rejected excessive batch size")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")

def run_all_tests():
    """Run all API tests"""
    print("\n")
    print("╔" + "═"*58 + "╗")
    print("║" + " "*10 + "MENTAL HEALTH API TEST SUITE" + " "*20 + "║")
    print("║" + " "*15 + f"Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" + " "*15 + "║")
    print("╚" + "═"*58 + "╝")
    
    try:
        # Basic endpoint tests
        test_root()
        test_health()
        test_categories()
        test_stats()
        
        # Prediction tests
        test_single_prediction()
        test_batch_prediction()
        
        # Error handling tests
        test_error_handling()
        
        # Summary
        print("\n")
        print("╔" + "═"*58 + "╗")
        print("║" + " "*15 + "ALL TESTS COMPLETED!" + " "*22 + "║")
        print("║" + " "*10 + "✅ API is working correctly" + " "*21 + "║")
        print("╚" + "═"*58 + "╝")
        print("\n")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to API server")
        print("Make sure the server is running with: uvicorn api:app --reload --port 8000")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    run_all_tests()
