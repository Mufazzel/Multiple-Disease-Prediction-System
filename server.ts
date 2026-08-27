import express from "express";
import path from "path";
import { execFile } from "child_process";
import { createServer as createViteServer } from "vite";

async function startServer() {
  const app = express();
  const PORT = 3000;

  // JSON Body Parser
  app.use(express.json({ limit: "10mb" }));

  // Python ML execution helper
  const runPythonPrediction = (
    modelName: string,
    payload: any
  ): Promise<any> => {
    return new Promise((resolve, reject) => {
      const scriptPath = path.join(process.cwd(), "python", "predict.py");
      const payloadStr = JSON.stringify(payload);

      execFile(
        "python3",
        [scriptPath, modelName, payloadStr],
        {
          cwd: path.join(process.cwd(), "python"),
          timeout: 15000,
          maxBuffer: 10 * 1024 * 1024,
        },
        (error, stdout, stderr) => {
          if (error) {
            console.error(`Python execution error (${modelName}):`, stderr || error.message);
            return reject(new Error(stderr || error.message));
          }
          try {
            const parsed = JSON.parse(stdout.trim());
            resolve(parsed);
          } catch (e) {
            console.error("Failed to parse Python JSON output:", stdout);
            reject(new Error("Invalid output format from Python ML script"));
          }
        }
      );
    });
  };

  // --- API Routes ---

  // Health and Python Engine Status
  app.get("/api/health", (_req, res) => {
    res.json({
      status: "ok",
      timestamp: new Date().toISOString(),
      engine: "Python 3.10 Backend Machine Learning Service",
    });
  });

  app.get("/api/python-status", (_req, res) => {
    execFile("python3", ["--version"], (error, stdout, stderr) => {
      res.json({
        available: !error,
        version: stdout.trim() || stderr.trim() || "Python 3.10",
        models: [
          { name: "Diabetes SVM Classifier", file: "python/diabetes_model.py" },
          { name: "Heart Disease Logistic Regression", file: "python/heart_disease_model.py" },
          { name: "Parkinson's SVC", file: "python/parkinsons_model.py" },
        ],
      });
    });
  });

  // Diabetes Prediction endpoint
  app.post("/api/predict/diabetes", async (req, res) => {
    try {
      const result = await runPythonPrediction("diabetes", req.body);
      res.json(result);
    } catch (err: any) {
      res.status(500).json({
        error: "Failed to execute Python diabetes model",
        details: err.message,
      });
    }
  });

  // Heart Disease Prediction endpoint
  app.post("/api/predict/heart", async (req, res) => {
    try {
      const result = await runPythonPrediction("heart", req.body);
      res.json(result);
    } catch (err: any) {
      res.status(500).json({
        error: "Failed to execute Python heart disease model",
        details: err.message,
      });
    }
  });

  // Parkinson's Prediction endpoint
  app.post("/api/predict/parkinsons", async (req, res) => {
    try {
      const result = await runPythonPrediction("parkinsons", req.body);
      res.json(result);
    } catch (err: any) {
      res.status(500).json({
        error: "Failed to execute Python Parkinson's model",
        details: err.message,
      });
    }
  });

  // Batch evaluation endpoint
  app.post("/api/predict/batch", async (req, res) => {
    try {
      const result = await runPythonPrediction("batch", req.body);
      res.json(result);
    } catch (err: any) {
      res.status(500).json({
        error: "Failed to execute Python batch model",
        details: err.message,
      });
    }
  });

  // --- Vite Dev Middleware or Production Static Serving ---
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), "dist");
    app.use(express.static(distPath));
    app.get("*", (_req, res) => {
      res.sendFile(path.join(distPath, "index.html"));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`MedPredict AI Server running on port ${PORT}`);
  });
}

startServer().catch((err) => {
  console.error("Failed to start server:", err);
  process.exit(1);
});
