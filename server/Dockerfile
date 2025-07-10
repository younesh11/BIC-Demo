# ---------------------------------------------
# Younesh KC
# ---------------------------------------------
FROM ubuntu:22.04
 
# Install build dependencies (including libcurl for llama_server)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      git \
      ca-certificates \
      cmake \
      wget \
      libcurl4-openssl-dev && \
    rm -rf /var/lib/apt/lists/*
 
# ---------------------------------------------
# 2) Clone llama.cpp
# ---------------------------------------------
WORKDIR /opt
RUN git clone https://github.com/ggml-org/llama.cpp.git
 
# ---------------------------------------------
# 3) Build HTTP server (Release, SIMD + OpenMP)
# ---------------------------------------------
WORKDIR /opt/llama.cpp
RUN mkdir build && \
    cd build && \
    cmake .. \
      -DCMAKE_BUILD_TYPE=Release \
      -DLLAMA_SERVER=ON \
      -DCMAKE_C_FLAGS="-O3 -march=native -fopenmp" \
      -DCMAKE_CXX_FLAGS="-O3 -march=native -fopenmp" && \
    make -j$(nproc) && \
    \
 
 
    if [ -f /opt/llama.cpp/build/llama_server ]; then \
      cp /opt/llama.cpp/build/llama_server /usr/local/bin/llama_server; \
    elif [ -f /opt/llama.cpp/build/bin/llama_server ]; then \
      cp /opt/llama.cpp/build/bin/llama_server /usr/local/bin/llama_server; \
    else \
      FOUND="$(find /opt/llama.cpp/build -maxdepth 2 -type f -executable | grep -i server | head -n1)" && \
      if [ -n "$FOUND" ]; then \
        cp "$FOUND" /usr/local/bin/llama_server; \
      else \
        echo "ERROR: llama_server not found in build output!" >&2 && exit 1; \
      fi; \
    fi && \
    chmod +x /usr/local/bin/llama_server
 
 
RUN mkdir -p /models
COPY models/Llama-3.2-1B-Instruct-Q3_K_S.gguf /models/Llama-3.2-1B-Instruct-Q3_K_S.gguf
 
 
EXPOSE 8080
 
ENV OMP_NUM_THREADS=4
 
 
CMD ["/usr/local/bin/llama_server", \
     "--host", "0.0.0.0", \
     "--port", "8080", \
     "--model", "/models/Llama-3.2-1B-Instruct-Q3_K_S.gguf"]