# My Project Hypotheses (Written BEFORE running experiments)

## Why are we writing these hypotheses first?
In scientific machine learning, we must write our predictions **before** running any tests. This proves to our evaluator that we didn't just look at the final code results and pretend we knew them all along! We are using Git timestamps to lock in these guesses.

---

## 1. Context & The Problem We Are Solving (In Simple Terms)

* **What works right now:** PatchCore is an AI algorithm used in factories to spot defective products (anomalies). Under perfect, steady studio lighting, it gets almost 100% of its predictions right.
* **The real-world problem:** In a real factory, lighting changes constantly (sunlight shifts through windows, shadows from machinery, aging lightbulbs).
* **What happens to the AI:** When lighting changes, PatchCore freaks out! It calculates higher "anomaly scores" for normal, good products and flags them as broken. This creates a high rate of **false alarms**.
* **Our goal:** Test 3 lightweight fixes (B1: Adding light variations to memory, B2: Re-aligning feature averages, B3: Auto-adjusting the decision cutoff line) to stop these false alarms without retraining the heavy AI model.

---

## 2. Key Terms & Parameters Explained Simply

* **Alpha ($\alpha = 0.05$):** Our target false alarm budget. $\alpha = 0.05$ means we accept a maximum of 5% false alarms on good items.
* **$n$ (Target Images):** The tiny set of normal photos (e.g., 5 or 20 images) taken under the new factory lighting that we use to adjust our model.
* **AUROC (Ranking score):** Measures how well the AI ranks defective items above normal items. (1.0 is perfect ranking, 0.5 is guessing).
* **F1-Score / FPR (Cutoff score):** Measures how well our threshold cutoff works. Even if ranking is high, a bad threshold ruins the F1-score because of false alarms.
* **Layer 2 vs. Layer 3:** `layer2` in the AI sees basic colors, textures, and lighting. `layer3` sees bigger shapes and structural objects.

---

## 3. Our 6 Main Predictions (QR1 to QR6)

### QR1: Lighting affects early layers more than deep layers.
* **Our Logic:** Because `layer2` looks at lighting and shadows, light shifts will confuse it heavily. But `layer3` looks at object shapes, so light shifts won't bother it as much.
* **Prediction:** `layer2` statistic drift will strongly correlate with accuracy drop (Spearman correlation $\rho \le -0.75$). `layer3` will have a much weaker correlation ($\rho \le -0.45$).

### QR2: The AI still knows what's broken, but its threshold line gets ruined.
* **Our Logic:** When lighting changes, the anomaly score of *everything* (good items and bad items) goes up together. Because everything shifts up equally, bad items are still ranked higher than good items (so AUROC stays high). But because good items now cross the old cutoff line, false alarms skyrocket (so F1 collapses).
* **Prediction:** AUROC will drop very little ($\le 0.08$ points), but F1-score at the old threshold will drop massively ($\ge 0.40$ points).

### QR3: B2 fixes ranking, B3 fixes the threshold cutoff.
* **Our Logic:** Feature alignment (B2) shifts the raw scores back to normal so ranking works again. Conformal calibration (B3) recalculates a smart cutoff line to directly stop false alarms.

### QR4: How many new photos ($n$) do we need to fix the model?
* **Our Logic:** If we only use 1 or 2 new photos, our new threshold will be wildly inaccurate. But once we give it around 20 photos ($n=20$), the math stabilizes.
* **Prediction:** At $n = 20$ target photos, our false alarm error will be within $0.02$ of our $0.05$ goal (meaning real false alarms will stay safely between 3% and 7%).

### QR5: Speed and Memory Costs.
* **Our Logic:** B2 and B3 are just simple math formulas, so they take almost zero computer time. B1 saves extra images into memory, so it uses more RAM.
* **Prediction:** B2 and B3 add less than $5\text{ ms}$ of delay per image. B1 doubles ($2\times$) the memory size.

### QR6: Where will our method fail?
* **Our Logic:** Our fixes are built specifically for *lighting* changes. If an image becomes blurry or distorted, channel alignment won't be enough to fix it.

---

## 4. Ground Rules for Testing
* Target false alarm rate ($\alpha$) is set to $0.05$.
* Lighting severity tested at levels 1 (light change), 3 (medium), and 5 (extreme).
* We tune settings on Validation data ONLY—never on Test data!