class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_max=1.0):
        self.ph_min, self.ph_max = ph_range
        self.turbidity_max = turbidity_max

    def check_safety(self, sensor):
        ph = sensor['ph']
        turbidity = sensor['turbidity']
        
        if ph is None:
            return "❌ Unsafe (missing pH)"
        if turbidity is None:
            return "❌ Unsafe (missing turbidity)"
        if ph < self.ph_min:
            return "❌ Unsafe (pH too low)"
        if ph > self.ph_max:
            return "❌ Unsafe (pH too high)"
        if turbidity > self.turbidity_max:
            return "❌ Unsafe (turbidity too high)"
        return "✅ Safe"
