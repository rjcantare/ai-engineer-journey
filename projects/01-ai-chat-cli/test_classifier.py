import unittest
import json

from main import classify_risk, validate_features


class TestRiskClassifier(unittest.TestCase):

    # ---------------------------
    # CLASSIFIER TESTS
    # ---------------------------

    def test_hot_above_threshold(self):
        self.assertEqual(classify_risk(85), "HOT")

    def test_hot_boundary_70(self):
        self.assertEqual(classify_risk(70), "HOT")

    def test_warm_69(self):
        self.assertEqual(classify_risk(69), "WARM")

    def test_warm_40(self):
        self.assertEqual(classify_risk(40), "WARM")

    def test_cold_39(self):
        self.assertEqual(classify_risk(39), "COLD")


class TestValidation(unittest.TestCase):

    def valid_payload(self):
        return {
            "risk_score": 50,
            "income_level": "medium",
            "dependency_load": "moderate",
            "savings_buffer": "moderate"
        }

    # ---------------------------
    # VALID STRUCTURE TEST
    # ---------------------------

    def test_valid_payload_passes(self):
        payload = self.valid_payload()
        raw = json.dumps(payload)
        result = validate_features(raw)
        self.assertEqual(result, payload)

    # ---------------------------
    # VALIDATION FAILURE TESTS
    # ---------------------------

    def test_missing_key(self):
        payload = self.valid_payload()
        del payload["income_level"]
        raw = json.dumps(payload)

        with self.assertRaises(ValueError):
            validate_features(raw)

    def test_extra_key(self):
        payload = self.valid_payload()
        payload["extra"] = "not_allowed"
        raw = json.dumps(payload)

        with self.assertRaises(ValueError):
            validate_features(raw)

    def test_risk_score_out_of_range(self):
        payload = self.valid_payload()
        payload["risk_score"] = 150
        raw = json.dumps(payload)

        with self.assertRaises(ValueError):
            validate_features(raw)

    def test_risk_score_not_integer(self):
        payload = self.valid_payload()
        payload["risk_score"] = 75.5
        raw = json.dumps(payload)

        with self.assertRaises(ValueError):
            validate_features(raw)


if __name__ == "__main__":
    unittest.main()