class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        // const m = Math.floor(h/piles.length);
        const maxim = piles.reduce((i,j) => Math.max(i, j), 0);
        // const upperBound = Math.ceil(maxim/m);
        const check = k => {
            let result = true;
            let totalHours = 0;
            for (let i = 0; i < piles.length; ++i) {
                totalHours += Math.ceil(piles[i] / k);
                if (totalHours > h) {
                    result = false;
                    break;
                }
            }
            return result;
        }

        const search = (low, high) => {
            const mid = parseInt(low + (high - low) / 2);
            console.log(low, high, mid);
            if (low == high) {
                return low;
            }
            if (check(mid)) {
                return search(low, mid);
            } else {
                return search(mid + 1, high);
            }
        }

        return search(1, maxim);
    }
}
