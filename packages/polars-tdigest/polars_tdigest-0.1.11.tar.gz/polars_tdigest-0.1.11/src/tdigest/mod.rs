/*
 * Original version created by by Paul Meng and distributed under Apache-2.0 license.
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * https://github.com/MnO2/t-digest
 *
 */

pub mod codecs;

use ordered_float::OrderedFloat;
use std::cmp::Ordering;

use serde::{Deserialize, Serialize};

/// Centroid implementation to the cluster mentioned in the paper.
#[derive(Debug, PartialEq, Eq, Clone, Serialize, Deserialize)]
pub struct Centroid {
    mean: OrderedFloat<f64>,
    weight: OrderedFloat<f64>,
}

impl PartialOrd for Centroid {
    fn partial_cmp(&self, other: &Centroid) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Centroid {
    fn cmp(&self, other: &Centroid) -> Ordering {
        self.mean.cmp(&other.mean)
    }
}

impl Centroid {
    pub fn new(mean: f64, weight: f64) -> Self {
        Centroid {
            mean: OrderedFloat::from(mean),
            weight: OrderedFloat::from(weight),
        }
    }

    #[inline]
    pub fn mean(&self) -> f64 {
        self.mean.into_inner()
    }

    #[inline]
    pub fn weight(&self) -> f64 {
        self.weight.into_inner()
    }

    pub fn add(&mut self, sum: f64, weight: f64) -> f64 {
        let weight_: f64 = self.weight.into_inner();
        let mean_: f64 = self.mean.into_inner();

        let new_sum: f64 = sum + weight_ * mean_;
        let new_weight: f64 = weight_ + weight;
        self.weight = OrderedFloat::from(new_weight);
        self.mean = OrderedFloat::from(new_sum / new_weight);
        new_sum
    }
}

impl Default for Centroid {
    fn default() -> Self {
        Centroid {
            mean: OrderedFloat::from(0.0),
            weight: OrderedFloat::from(1.0),
        }
    }
}

/// T-Digest to be operated on.
#[derive(Debug, PartialEq, Eq, Clone, Serialize, Deserialize)]
pub struct TDigest {
    centroids: Vec<Centroid>,
    max_size: usize,
    sum: OrderedFloat<f64>,
    count: OrderedFloat<f64>,
    max: OrderedFloat<f64>,
    min: OrderedFloat<f64>,
}

impl TDigest {
    pub fn new_with_size(max_size: usize) -> Self {
        TDigest {
            centroids: Vec::new(),
            max_size,
            sum: OrderedFloat::from(0.0),
            count: OrderedFloat::from(0.0),
            max: OrderedFloat::from(f64::NAN),
            min: OrderedFloat::from(f64::NAN),
        }
    }

    pub fn new(
        centroids: Vec<Centroid>,
        sum: f64,
        count: f64,
        max: f64,
        min: f64,
        max_size: usize,
    ) -> Self {
        if centroids.len() <= max_size {
            TDigest {
                centroids,
                max_size,
                sum: OrderedFloat::from(sum),
                count: OrderedFloat::from(count),
                max: OrderedFloat::from(max),
                min: OrderedFloat::from(min),
            }
        } else {
            let sz = centroids.len();
            let digests: Vec<TDigest> = vec![
                TDigest::new_with_size(100),
                TDigest::new(centroids, sum, count, max, min, sz),
            ];

            Self::merge_digests(digests)
        }
    }

    #[inline]
    pub fn mean(&self) -> f64 {
        let count_: f64 = self.count.into_inner();
        let sum_: f64 = self.sum.into_inner();

        if count_ > 0.0 {
            sum_ / count_
        } else {
            0.0
        }
    }

    #[inline]
    pub fn sum(&self) -> f64 {
        self.sum.into_inner()
    }

    #[inline]
    pub fn count(&self) -> f64 {
        self.count.into_inner()
    }

    #[inline]
    pub fn max(&self) -> f64 {
        self.max.into_inner()
    }

    #[inline]
    pub fn min(&self) -> f64 {
        self.min.into_inner()
    }

    #[inline]
    pub fn is_empty(&self) -> bool {
        self.centroids.is_empty()
    }

    #[inline]
    pub fn max_size(&self) -> usize {
        self.max_size
    }

    #[inline]
    pub fn centroids(&self) -> &Vec<Centroid> {
        &self.centroids
    }
}

impl Default for TDigest {
    fn default() -> Self {
        TDigest {
            centroids: Vec::new(),
            max_size: 100,
            sum: OrderedFloat::from(0.0),
            count: OrderedFloat::from(0.0),
            max: OrderedFloat::from(f64::NAN),
            min: OrderedFloat::from(f64::NAN),
        }
    }
}

impl TDigest {
    fn k_to_q(k: f64, d: f64) -> f64 {
        let k_div_d = k / d;
        if k_div_d >= 0.5 {
            let base = 1.0 - k_div_d;
            1.0 - 2.0 * base * base
        } else {
            2.0 * k_div_d * k_div_d
        }
    }

    fn clamp(v: f64, lo: f64, hi: f64) -> f64 {
        if v > hi {
            hi
        } else if v < lo {
            lo
        } else {
            v
        }
    }

    // See
    // https://github.com/protivinsky/pytdigest/blob/main/pytdigest/tdigest.c#L300-L336
    pub fn estimate_cdf(&self, val: f64) -> f64 {
        if self.centroids.is_empty() {
            return f64::NAN;
        }

        let mut running_total_weight = 0.0;
        let mut matched_centroid: Option<(usize, &Centroid)> = None;

        for (index, centroid) in self.centroids.iter().enumerate() {
            if centroid.mean() >= val {
                matched_centroid = Some((index, centroid));
                break;
            }
            running_total_weight += centroid.weight();
        }

        match matched_centroid {
            Some((centroid_index, current_centroid)) => {
                if val == current_centroid.mean() {
                    let mut weight_at_value = current_centroid.weight();
                    for centroid in &self.centroids[centroid_index + 1..] {
                        if centroid.mean() == current_centroid.mean() {
                            weight_at_value += centroid.weight();
                        } else {
                            break;
                        }
                    }
                    return (running_total_weight + (weight_at_value / 2.0)) / self.count();
                } else if centroid_index == 0 {
                    return 0.0;
                }

                let cr = current_centroid;
                let cl = &self.centroids[centroid_index - 1];
                running_total_weight -= cl.weight() / 2.0;

                let m = (cr.mean() - cl.mean()) / (cl.weight() / 2.0 + cr.weight() / 2.0);
                let x = (val - cl.mean()) / m;
                (running_total_weight + x) / self.count()
            }
            None => 1.0, // No centroid matched the condition, meaning `val` is greater than all centroids
        }
    }

    pub fn merge_unsorted(&self, unsorted_values: Vec<f64>) -> TDigest {
        let mut sorted_values: Vec<OrderedFloat<f64>> = unsorted_values
            .into_iter()
            .map(OrderedFloat::from)
            .collect();
        sorted_values.sort();
        let sorted_values = sorted_values.into_iter().map(|f| f.into_inner()).collect();

        self.merge_sorted(sorted_values)
    }

    pub fn merge_sorted(&self, sorted_values: Vec<f64>) -> TDigest {
        if sorted_values.is_empty() {
            return self.clone();
        }

        let mut result = TDigest::new_with_size(self.max_size());
        result.count = OrderedFloat::from(self.count() + (sorted_values.len() as f64));

        let maybe_min = OrderedFloat::from(*sorted_values.first().unwrap());
        let maybe_max = OrderedFloat::from(*sorted_values.last().unwrap());

        if self.count() > 0.0 {
            result.min = std::cmp::min(self.min, maybe_min);
            result.max = std::cmp::max(self.max, maybe_max);
        } else {
            result.min = maybe_min;
            result.max = maybe_max;
        }

        let mut compressed: Vec<Centroid> = Vec::with_capacity(self.max_size);

        let mut k_limit: f64 = 1.0;
        let mut q_limit_times_count: f64 =
            Self::k_to_q(k_limit, self.max_size as f64) * result.count.into_inner();
        k_limit += 1.0;

        let mut iter_centroids = self.centroids.iter().peekable();
        let mut iter_sorted_values = sorted_values.iter().peekable();

        let mut curr: Centroid = if let Some(c) = iter_centroids.peek() {
            let curr = **iter_sorted_values.peek().unwrap();
            if c.mean() < curr {
                iter_centroids.next().unwrap().clone()
            } else {
                Centroid::new(*iter_sorted_values.next().unwrap(), 1.0)
            }
        } else {
            Centroid::new(*iter_sorted_values.next().unwrap(), 1.0)
        };

        let mut weight_so_far: f64 = curr.weight();

        let mut sums_to_merge: f64 = 0.0;
        let mut weights_to_merge: f64 = 0.0;

        while iter_centroids.peek().is_some() || iter_sorted_values.peek().is_some() {
            let next: Centroid = if let Some(c) = iter_centroids.peek() {
                if iter_sorted_values.peek().is_none()
                    || c.mean() < **iter_sorted_values.peek().unwrap()
                {
                    iter_centroids.next().unwrap().clone()
                } else {
                    Centroid::new(*iter_sorted_values.next().unwrap(), 1.0)
                }
            } else {
                Centroid::new(*iter_sorted_values.next().unwrap(), 1.0)
            };

            let next_sum: f64 = next.mean() * next.weight();
            weight_so_far += next.weight();

            if weight_so_far <= q_limit_times_count {
                sums_to_merge += next_sum;
                weights_to_merge += next.weight();
            } else {
                result.sum = OrderedFloat::from(
                    result.sum.into_inner() + curr.add(sums_to_merge, weights_to_merge),
                );
                sums_to_merge = 0.0;
                weights_to_merge = 0.0;

                compressed.push(curr.clone());
                q_limit_times_count = Self::k_to_q(k_limit, self.max_size as f64) * result.count();
                k_limit += 1.0;
                curr = next;
            }
        }

        result.sum =
            OrderedFloat::from(result.sum.into_inner() + curr.add(sums_to_merge, weights_to_merge));
        compressed.push(curr);
        compressed.shrink_to_fit();
        compressed.sort();

        result.centroids = compressed;
        result
    }

    fn external_merge(centroids: &mut [Centroid], first: usize, middle: usize, last: usize) {
        let mut result: Vec<Centroid> = Vec::with_capacity(centroids.len());

        let mut i = first;
        let mut j = middle;

        while i < middle && j < last {
            match centroids[i].cmp(&centroids[j]) {
                Ordering::Less => {
                    result.push(centroids[i].clone());
                    i += 1;
                }
                Ordering::Greater => {
                    result.push(centroids[j].clone());
                    j += 1;
                }
                Ordering::Equal => {
                    result.push(centroids[i].clone());
                    i += 1;
                }
            }
        }

        while i < middle {
            result.push(centroids[i].clone());
            i += 1;
        }

        while j < last {
            result.push(centroids[j].clone());
            j += 1;
        }

        i = first;
        for centroid in result.into_iter() {
            centroids[i] = centroid;
            i += 1;
        }
    }

    // Merge multiple T-Digests
    pub fn merge_digests(digests: Vec<TDigest>) -> TDigest {
        let n_centroids: usize = digests.iter().map(|d| d.centroids.len()).sum();
        if n_centroids == 0 {
            return TDigest::default();
        }

        let max_size = digests.first().unwrap().max_size;
        let mut centroids: Vec<Centroid> = Vec::with_capacity(n_centroids);
        let mut starts: Vec<usize> = Vec::with_capacity(digests.len());

        let mut count: f64 = 0.0;
        let mut min = OrderedFloat::from(f64::INFINITY);
        let mut max = OrderedFloat::from(f64::NEG_INFINITY);

        let mut start: usize = 0;
        for digest in digests.into_iter() {
            starts.push(start);

            let curr_count: f64 = digest.count();
            if curr_count > 0.0 {
                min = std::cmp::min(min, digest.min);
                max = std::cmp::max(max, digest.max);
                count += curr_count;
                for centroid in digest.centroids {
                    centroids.push(centroid);
                    start += 1;
                }
            }
        }

        let mut digests_per_block: usize = 1;
        while digests_per_block < starts.len() {
            for i in (0..starts.len()).step_by(digests_per_block * 2) {
                if i + digests_per_block < starts.len() {
                    let first = starts[i];
                    let middle = starts[i + digests_per_block];
                    let last = if i + 2 * digests_per_block < starts.len() {
                        starts[i + 2 * digests_per_block]
                    } else {
                        centroids.len()
                    };

                    debug_assert!(first <= middle && middle <= last);
                    Self::external_merge(&mut centroids, first, middle, last);
                }
            }

            digests_per_block *= 2;
        }

        let mut result = TDigest::new_with_size(max_size);
        let mut compressed: Vec<Centroid> = Vec::with_capacity(max_size);

        let mut k_limit: f64 = 1.0;
        let mut q_limit_times_count: f64 = Self::k_to_q(k_limit, max_size as f64) * count;

        let mut iter_centroids = centroids.iter_mut();
        let mut curr = iter_centroids.next().unwrap();
        let mut weight_so_far: f64 = curr.weight();
        let mut sums_to_merge: f64 = 0.0;
        let mut weights_to_merge: f64 = 0.0;

        for centroid in iter_centroids {
            weight_so_far += centroid.weight();

            if weight_so_far <= q_limit_times_count {
                sums_to_merge += centroid.mean() * centroid.weight();
                weights_to_merge += centroid.weight();
            } else {
                result.sum = OrderedFloat::from(
                    result.sum.into_inner() + curr.add(sums_to_merge, weights_to_merge),
                );
                sums_to_merge = 0.0;
                weights_to_merge = 0.0;
                compressed.push(curr.clone());
                q_limit_times_count = Self::k_to_q(k_limit, max_size as f64) * count;
                k_limit += 1.0;
                curr = centroid;
            }
        }

        result.sum =
            OrderedFloat::from(result.sum.into_inner() + curr.add(sums_to_merge, weights_to_merge));
        compressed.push(curr.clone());
        compressed.shrink_to_fit();
        compressed.sort();

        result.count = OrderedFloat::from(count);
        result.min = min;
        result.max = max;
        result.centroids = compressed;
        result
    }

    /// To estimate the value located at `q` quantile
    pub fn estimate_quantile(&self, q: f64) -> f64 {
        if self.centroids.is_empty() {
            return 0.0;
        }

        let count_: f64 = self.count.into_inner();
        let rank: f64 = q * count_;

        let mut pos: usize;
        let mut t: f64;
        if q > 0.5 {
            if q >= 1.0 {
                return self.max();
            }

            pos = 0;
            t = count_;

            for (k, centroid) in self.centroids.iter().enumerate().rev() {
                t -= centroid.weight();

                if rank >= t {
                    pos = k;
                    break;
                }
            }
        } else {
            if q <= 0.0 {
                return self.min();
            }

            pos = self.centroids.len() - 1;
            t = 0.0;

            for (k, centroid) in self.centroids.iter().enumerate() {
                if rank < t + centroid.weight() {
                    pos = k;
                    break;
                }

                t += centroid.weight();
            }
        }

        let mut delta = 0.0;
        let mut min: f64 = self.min.into_inner();
        let mut max: f64 = self.max.into_inner();

        if self.centroids.len() > 1 {
            if pos == 0 {
                delta = self.centroids[pos + 1].mean() - self.centroids[pos].mean();
                max = self.centroids[pos + 1].mean();
            } else if pos == (self.centroids.len() - 1) {
                delta = self.centroids[pos].mean() - self.centroids[pos - 1].mean();
                min = self.centroids[pos - 1].mean();
            } else {
                delta = (self.centroids[pos + 1].mean() - self.centroids[pos - 1].mean()) / 2.0;
                min = self.centroids[pos - 1].mean();
                max = self.centroids[pos + 1].mean();
            }
        }

        let value =
            self.centroids[pos].mean() + ((rank - t) / self.centroids[pos].weight() - 0.5) * delta;
        Self::clamp(value, min, max)
    }

    fn find_median_between_centroids(&self) -> Option<f64> {
        if (self.count.into_inner() as i64) % 2 != 0 {
            return None;
        }
        let mut target = (self.count.into_inner() as i64) / 2;
        for (idx, c) in self.centroids.iter().enumerate() {
            target -= c.weight() as i64;
            if target == 0 {
                let m1 = c.mean();
                let m2 = self.centroids[idx + 1].mean();
                return Option::Some((m1 + m2) / 2.0);
            }
            if target < 0 {
                return Option::None;
            }
        }
        Option::None
    }

    pub fn estimate_median(&self) -> f64 {
        /*
         * If the number of elements is even, median is average of two adjacent observation.
         * Interpolation algorithm used in `estimate_quantile` often positions estimated median too far away from the middle point.
         * So let's detect the case when the median is exactly between two centroids.
         */
        self.find_median_between_centroids()
            .unwrap_or(self.estimate_quantile(0.5))
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_centroid_addition_regression() {
        //https://github.com/MnO2/t-digest/pull/1

        let vals = vec![1.0, 1.0, 1.0, 2.0, 1.0, 1.0];
        let mut t = TDigest::new_with_size(10);

        for v in vals {
            t = t.merge_unsorted(vec![v]);
        }

        let ans = t.estimate_quantile(0.5);
        let expected: f64 = 1.0;
        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.95);
        let expected: f64 = 2.0;
        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);
    }

    #[test]
    fn test_merge_sorted_against_uniform_distro() {
        let t = TDigest::new_with_size(100);
        let values: Vec<f64> = (1..=1_000_000).map(f64::from).collect();

        let t = t.merge_sorted(values);

        let ans = t.estimate_quantile(1.0);
        let expected: f64 = 1_000_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.99);
        let expected: f64 = 990_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.01);
        let expected: f64 = 10_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.0);
        let expected: f64 = 1.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.5);
        let expected: f64 = 500_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);
    }

    #[test]
    fn test_merge_unsorted_against_uniform_distro() {
        let t = TDigest::new_with_size(100);
        let values: Vec<f64> = (1..=1_000_000).map(f64::from).collect();

        let t = t.merge_unsorted(values);

        let ans = t.estimate_quantile(1.0);
        let expected: f64 = 1_000_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.99);
        let expected: f64 = 990_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.01);
        let expected: f64 = 10_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.0);
        let expected: f64 = 1.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.5);
        let expected: f64 = 500_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);
    }

    #[test]
    fn test_merge_sorted_against_skewed_distro() {
        let t = TDigest::new_with_size(100);
        let mut values: Vec<f64> = (1..=600_000).map(f64::from).collect();
        for _ in 0..400_000 {
            values.push(1_000_000.0);
        }

        let t = t.merge_sorted(values);

        let ans = t.estimate_quantile(0.99);
        let expected: f64 = 1_000_000.0;
        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.01);
        let expected: f64 = 10_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.5);
        let expected: f64 = 500_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);
    }

    #[test]
    fn test_merge_unsorted_against_skewed_distro() {
        let t = TDigest::new_with_size(100);
        let mut values: Vec<f64> = (1..=600_000).map(f64::from).collect();
        for _ in 0..400_000 {
            values.push(1_000_000.0);
        }

        let t = t.merge_unsorted(values);

        let ans = t.estimate_quantile(0.99);
        let expected: f64 = 1_000_000.0;
        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.01);
        let expected: f64 = 10_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.5);
        let expected: f64 = 500_000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);
    }

    #[test]
    fn test_merge_digests() {
        let mut digests: Vec<TDigest> = Vec::new();

        for _ in 1..=100 {
            let t = TDigest::new_with_size(100);
            let values: Vec<f64> = (1..=1_000).map(f64::from).collect();
            let t = t.merge_sorted(values);
            digests.push(t)
        }

        let t = TDigest::merge_digests(digests);

        let ans = t.estimate_quantile(1.0);
        let expected: f64 = 1000.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.99);
        let expected: f64 = 990.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.01);
        let expected: f64 = 10.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.2);

        let ans = t.estimate_quantile(0.0);
        let expected: f64 = 1.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);

        let ans = t.estimate_quantile(0.5);
        let expected: f64 = 500.0;

        let percentage: f64 = (expected - ans).abs() / expected;
        assert!(percentage < 0.01);
    }

    #[test]
    fn test_median_between_centroids() {
        // median of [-1, -1, ..., 1, 1] should be ~0
        let mut quantile_didnt_work: bool = false;
        for num in [1, 2, 3, 10, 20] {
            let mut t = TDigest::new_with_size(100);
            for _ in 1..=num {
                t = t.merge_sorted(vec![-1.0]);
            }
            for _ in 1..=num {
                t = t.merge_sorted(vec![1.0]);
            }

            if t.estimate_quantile(0.5).abs() > 0.1 {
                quantile_didnt_work = true;
            }

            assert!(t.estimate_median().abs() < 0.01);
        }
        assert!(quantile_didnt_work);
    }

    #[test]
    fn test_cdf() {
        let t = TDigest::new_with_size(100);
        let values: Vec<f64> = vec![1.0, 2.0, 3.0, 4.0, 5.0];
        let t = t.merge_sorted(values);

        assert!(
            (t.estimate_cdf(3.0) - 0.5).abs() < 0.0001,
            "CDF(3.0) deviates from 0.5"
        );
        assert!(
            (t.estimate_cdf(1.0) - 0.1).abs() < 0.0001,
            "CDF(1.0) deviates from 0.1"
        );
        assert!(
            (t.estimate_cdf(5.0) - 0.9).abs() < 0.0001,
            "CDF(5.0) deviates from 0.9"
        );
        assert_eq!(t.estimate_cdf(0.0), 0.0, "CDF(0.0) should be 0.0");
        assert_eq!(t.estimate_cdf(6.0), 1.0, "CDF(6.0) should be 1.0");
    }

    #[test]
    fn test_cdf_out_of_bounds() {
        let t = TDigest::new_with_size(100);
        let values: Vec<f64> = vec![1.0, 2.0, 3.0, 4.0, 5.0];
        let t = t.merge_sorted(values);

        // Test when the value is less than the minimum element
        assert_eq!(t.estimate_cdf(0.0), 0.0, "CDF(0.0) should be 0.0");

        // Test when the value is greater than the maximum element
        assert_eq!(t.estimate_cdf(6.0), 1.0, "CDF(6.0) should be 1.0");
    }
}
