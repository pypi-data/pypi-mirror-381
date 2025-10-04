//! RAT Engine 错误处理模块
//! 
//! 提供统一的错误类型和处理机制

use std::fmt;

/// RAT Engine 错误类型
#[derive(Debug)]
pub enum RatError {
    /// 服务器配置错误
    ConfigError(String),
    /// 网络错误
    NetworkError(String),
    /// 缓存错误
    CacheError(String),
    /// 请求构建错误
    RequestError(String),
    /// 超时错误
    TimeoutError(String),
    /// 解码错误
    DecodingError(String),
    /// 路由错误
    RouteError(String),
    /// 工作池错误
    WorkerPoolError(String),
    /// 系统信息错误
    SystemInfoError(String),
    /// IO错误
    IoError(std::io::Error),
    /// Hyper错误
    HyperError(hyper::Error),
    /// Reqwest错误
    #[cfg(feature = "reqwest")]
    ReqwestError(reqwest::Error),
    /// 解析错误
    ParseError(String),
    /// 验证错误
    ValidationError(String),
    /// 安全错误
    SecurityError(String),
    /// TLS错误
    TlsError(String),
    /// 序列化错误
    SerializationError(String),
    /// 反序列化错误
    DeserializationError(String),
    /// Python错误
    PythonError(String),
    /// 智能传输错误
    TransferError(String),
    /// 无效参数错误
    InvalidArgument(String),
    /// 其他错误
    Other(String),
}

/// RAT Engine 专用错误类型（别名）
pub type RatEngineError = RatError;

impl fmt::Display for RatError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            RatError::ConfigError(msg) => write!(f, "Configuration error: {}", msg),
            RatError::NetworkError(msg) => write!(f, "Network error: {}", msg),
            RatError::CacheError(msg) => write!(f, "Cache error: {}", msg),
            RatError::RequestError(msg) => write!(f, "Request error: {}", msg),
            RatError::TimeoutError(msg) => write!(f, "Timeout error: {}", msg),
            RatError::DecodingError(msg) => write!(f, "Decoding error: {}", msg),
            RatError::RouteError(msg) => write!(f, "Route error: {}", msg),
            RatError::WorkerPoolError(msg) => write!(f, "Worker pool error: {}", msg),
            RatError::SystemInfoError(msg) => write!(f, "System info error: {}", msg),
            RatError::IoError(err) => write!(f, "IO error: {}", err),
            RatError::HyperError(err) => write!(f, "HTTP error: {}", err),
            RatError::ParseError(msg) => write!(f, "Parse error: {}", msg),
            RatError::ValidationError(msg) => write!(f, "Validation error: {}", msg),
            RatError::SecurityError(msg) => write!(f, "Security error: {}", msg),
            RatError::TlsError(msg) => write!(f, "TLS error: {}", msg),
            RatError::SerializationError(msg) => write!(f, "Serialization error: {}", msg),
            RatError::DeserializationError(msg) => write!(f, "Deserialization error: {}", msg),
            RatError::PythonError(msg) => write!(f, "Python error: {}", msg),
            RatError::TransferError(msg) => write!(f, "Transfer error: {}", msg),
            RatError::InvalidArgument(msg) => write!(f, "Invalid argument: {}", msg),
            #[cfg(feature = "reqwest")]
            RatError::ReqwestError(err) => write!(f, "HTTP client error: {}", err),
            RatError::Other(msg) => write!(f, "Error: {}", msg),
        }
    }
}

impl std::error::Error for RatError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            RatError::IoError(err) => Some(err),
            RatError::HyperError(err) => Some(err),
            _ => None,
        }
    }
}

// 错误转换实现
// 注意：zstd 0.12.4 版本使用 std::io::Error 而不是自定义的 Error 类型
// 因此不需要为 zstd::Error 实现 From trait，直接使用已有的 std::io::Error 实现

impl From<std::io::Error> for RatError {
    fn from(err: std::io::Error) -> Self {
        RatError::IoError(err)
    }
}


impl From<hyper::Error> for RatError {
    fn from(err: hyper::Error) -> Self {
        RatError::HyperError(err)
    }
}

#[cfg(feature = "reqwest")]
impl From<reqwest::Error> for RatError {
    fn from(err: reqwest::Error) -> Self {
        RatError::ReqwestError(err)
    }
}

impl From<std::net::AddrParseError> for RatError {
    fn from(err: std::net::AddrParseError) -> Self {
        RatError::ParseError(format!("Address parse error: {}", err))
    }
}

impl From<std::num::ParseIntError> for RatError {
    fn from(err: std::num::ParseIntError) -> Self {
        RatError::ParseError(format!("Integer parse error: {}", err))
    }
}


// 注意：std::io::Error 的转换已在上面实现

// Brotli 3.4.0 不再使用 brotli::error::Error，而是使用 std::io::Error
// 因此这里不需要特别的实现，会使用通用的 std::io::Error 实现

#[cfg(feature = "compression")]
impl From<flate2::CompressError> for RatError {
    fn from(err: flate2::CompressError) -> Self {
        RatError::IoError(std::io::Error::new(std::io::ErrorKind::Other, format!("Compression error: {}", err)))
    }
}

#[cfg(feature = "compression")]
impl From<flate2::DecompressError> for RatError {
    fn from(err: flate2::DecompressError) -> Self {
        RatError::IoError(std::io::Error::new(std::io::ErrorKind::Other, format!("Decompression error: {}", err)))
    }
}

// 注意：zstd 0.12.4 版本使用 std::io::Error 而不是自定义的 Error 类型
// 因此这里不需要重复实现 From<std::io::Error>

impl From<std::string::FromUtf8Error> for RatError {
    fn from(err: std::string::FromUtf8Error) -> Self {
        RatError::ValidationError(format!("Invalid UTF-8: {}", err))
    }
}

impl From<String> for RatError {
    fn from(msg: String) -> Self {
        RatError::Other(msg)
    }
}

#[cfg(feature = "cache")]
impl From<rat_memcache::error::CacheError> for RatError {
    fn from(err: rat_memcache::error::CacheError) -> Self {
        match err {
            rat_memcache::error::CacheError::IoError { source } => RatError::IoError(source),
            _ => RatError::Other(format!("Cache error: {}", err)),
        }
    }
}

/// RAT Engine 结果类型
pub type RatResult<T> = Result<T, RatError>;

/// 缓存错误类型
/// 
/// 对外暴露的缓存错误类型，隐藏 rat_memcache 的实现细节
#[derive(Debug)]
pub struct CacheError(RatError);

impl CacheError {
    /// 创建 IO 错误
    pub fn io_error(msg: &str) -> Self {
        CacheError(RatError::IoError(std::io::Error::new(std::io::ErrorKind::Other, msg)))
    }
    
    /// 创建配置错误
    pub fn config_error(msg: &str) -> Self {
        CacheError(RatError::ConfigError(msg.to_string()))
    }
    
    /// 创建验证错误
    pub fn validation_error(msg: &str) -> Self {
        CacheError(RatError::ValidationError(msg.to_string()))
    }
    
    /// 创建序列化错误
    pub fn serialization_error(msg: &str) -> Self {
        CacheError(RatError::SerializationError(msg.to_string()))
    }
    
    /// 创建反序列化错误
    pub fn deserialization_error(msg: &str) -> Self {
        CacheError(RatError::DeserializationError(msg.to_string()))
    }
    
    /// 创建其他错误
    pub fn other_error(msg: &str) -> Self {
        CacheError(RatError::Other(msg.to_string()))
    }
}

impl From<CacheError> for RatError {
    fn from(err: CacheError) -> Self {
        err.0
    }
}

impl From<std::io::Error> for CacheError {
    fn from(err: std::io::Error) -> Self {
        CacheError(RatError::IoError(err))
    }
}

impl fmt::Display for CacheError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl std::error::Error for CacheError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        self.0.source()
    }
}

/// 错误处理工具函数
pub mod utils {
    use super::*;

    /// 创建配置错误
    pub fn config_error(msg: &str) -> RatError {
        RatError::ConfigError(msg.to_string())
    }

    /// 创建网络错误
    pub fn network_error(msg: &str) -> RatError {
        RatError::NetworkError(msg.to_string())
    }

    /// 创建路由错误
    pub fn route_error(msg: &str) -> RatError {
        RatError::RouteError(msg.to_string())
    }

    /// 创建工作池错误
    pub fn worker_pool_error(msg: &str) -> RatError {
        RatError::WorkerPoolError(msg.to_string())
    }

    /// 创建系统信息错误
    pub fn system_info_error(msg: &str) -> RatError {
        RatError::SystemInfoError(msg.to_string())
    }

    /// 安全地解析字符串为数字
    pub fn safe_parse<T: std::str::FromStr>(s: &str, default: T) -> T
    where
        T::Err: std::fmt::Debug,
    {
        s.parse().unwrap_or(default)
    }

    /// 验证端口号
    pub fn validate_port(port: u16) -> RatResult<u16> {
        if port == 0 {
            Err(config_error("Port cannot be 0"))
        } else {
            Ok(port)
        }
    }

    /// 验证工作线程数
    pub fn validate_workers(workers: usize) -> RatResult<usize> {
        if workers == 0 {
            Err(config_error("Worker count cannot be 0"))
        } else if workers > 1024 {
            Err(config_error("Worker count cannot exceed 1024"))
        } else {
            Ok(workers)
        }
    }
}