import { create } from "zustand";

const useWaterStore = create((set) => ({
  prediction: null,
  loading: false,
  error: null,

  setPrediction: (data) => set({ prediction: data }),
  setLoading: (value) => set({ loading: value }),
  setError: (err) => set({ error: err })
}));

export default useWaterStore;
