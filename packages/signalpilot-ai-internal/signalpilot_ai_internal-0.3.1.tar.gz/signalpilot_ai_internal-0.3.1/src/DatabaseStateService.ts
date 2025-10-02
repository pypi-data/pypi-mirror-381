import { BehaviorSubject, Observable, Subject } from 'rxjs';
import { v4 as uuidv4 } from 'uuid';
import { DatabaseEncoder } from './utils/databaseEncoder';
import { DatabaseTools } from './BackendTools/DatabaseTools';
import { StateDBCachingService } from './utils/backendCaching';

/**
 * Supported database types
 */
export enum DatabaseType {
  MySQL = 'mysql',
  PostgreSQL = 'postgresql',
  Snowflake = 'snowflake'
}

/**
 * Base database credentials interface
 */
export interface IDatabaseCredentials {
  id: string;
  name: string;
  description: string;
  type: DatabaseType;
  host: string;
  port: number;
  database: string;
  username: string;
  password: string;
  // Created/updated timestamps
  createdAt: string;
  updatedAt: string;
}

/**
 * MySQL specific database credentials
 */
export interface IMySQLCredentials extends IDatabaseCredentials {
  type: DatabaseType.MySQL;
}

/**
 * PostgreSQL specific database credentials
 */
export interface IPostgreSQLCredentials extends IDatabaseCredentials {
  type: DatabaseType.PostgreSQL;
}

/**
 * Snowflake specific database credentials
 */
export interface ISnowflakeCredentials extends IDatabaseCredentials {
  type: DatabaseType.Snowflake;
  warehouse: string;
  role?: string;
  account: string;
}

/**
 * Database URL connection for URL-based connections
 */
export interface IDatabaseUrlConnection {
  id: string;
  name: string;
  description: string;
  type: DatabaseType;
  connectionUrl: string;
  // Created/updated timestamps
  createdAt: string;
  updatedAt: string;
}

/**
 * Database configuration (either credentials or URL-based)
 */
export interface IDatabaseConfig {
  id: string;
  name: string;
  type: DatabaseType;
  connectionType: 'credentials' | 'url';
  // Connection details (one will be null based on connectionType)
  credentials?:
    | IMySQLCredentials
    | IPostgreSQLCredentials
    | ISnowflakeCredentials;
  urlConnection?: IDatabaseUrlConnection;
  // Schema information
  schema_last_updated?: string | null;
  database_schema?: string | null;
  // Metadata
  createdAt: string;
  updatedAt: string;
}

/**
 * Database credentials state interface
 */
interface DatabaseCredentialsState {
  // Credential management
  configurations: IDatabaseConfig[];
  activeConfigId: string | null;
  activeConfig: IDatabaseConfig | null;

  // Service state
  isInitialized: boolean;
}

/**
 * Initial database credentials state
 */
const initialDatabaseCredentialsState: DatabaseCredentialsState = {
  // Configuration management
  configurations: [],
  activeConfigId: null,
  activeConfig: null,

  // Service state
  isInitialized: false
};

// State observable
const databaseCredentialsState$ = new BehaviorSubject<DatabaseCredentialsState>(
  initialDatabaseCredentialsState
);

// Event subjects for configuration changes
const configAdded$ = new Subject<IDatabaseConfig>();
const configRemoved$ = new Subject<{
  configId: string;
  config: IDatabaseConfig;
}>();
const configUpdated$ = new Subject<IDatabaseConfig>();
const activeConfigChanged$ = new Subject<{
  oldConfigId: string | null;
  newConfigId: string | null;
}>();

/**
 * Database Credentials State Service
 * Manages database credential configurations using RxJS
 */
export const DatabaseStateService = {
  /**
   * Get the current database credentials state
   */
  getState: () => databaseCredentialsState$.getValue(),

  /**
   * Update the database credentials state with partial values
   */
  setState: (partial: Partial<DatabaseCredentialsState>) =>
    databaseCredentialsState$.next({
      ...databaseCredentialsState$.getValue(),
      ...partial
    }),

  /**
   * Subscribe to state changes
   */
  changes: databaseCredentialsState$.asObservable(),

  /**
   * Initialize the database credentials service
   */
  initialize: () => {
    DatabaseStateService.setState({ isInitialized: true });
  },

  /**
   * Create a new MySQL database configuration using credentials
   */
  createMySQLConfig: (
    name: string,
    description: string,
    host: string,
    port: number,
    database: string,
    username: string,
    password: string
  ): IDatabaseConfig => {
    const id = uuidv4();
    const now = new Date().toISOString();

    const credentials: IMySQLCredentials = {
      id,
      name,
      description,
      type: DatabaseType.MySQL,
      host,
      port,
      database,
      username,
      password,
      createdAt: now,
      updatedAt: now
    };

    const config: IDatabaseConfig = {
      id,
      name,
      type: DatabaseType.MySQL,
      connectionType: 'credentials',
      credentials,
      urlConnection: undefined,
      schema_last_updated: null,
      database_schema: null,
      createdAt: now,
      updatedAt: now
    };

    // Add to configurations array
    const currentState = DatabaseStateService.getState();
    const updatedConfigurations = [...currentState.configurations, config];
    DatabaseStateService.setState({ configurations: updatedConfigurations });

    // Emit config added event
    configAdded$.next(config);

    return config;
  },

  /**
   * Create a new PostgreSQL database configuration using credentials
   */
  createPostgreSQLConfig: (
    name: string,
    description: string,
    host: string,
    port: number,
    database: string,
    username: string,
    password: string
  ): IDatabaseConfig => {
    const id = uuidv4();
    const now = new Date().toISOString();

    const credentials: IPostgreSQLCredentials = {
      id,
      name,
      description,
      type: DatabaseType.PostgreSQL,
      host,
      port,
      database,
      username,
      password,
      createdAt: now,
      updatedAt: now
    };

    const config: IDatabaseConfig = {
      id,
      name,
      type: DatabaseType.PostgreSQL,
      connectionType: 'credentials',
      credentials,
      urlConnection: undefined,
      schema_last_updated: null,
      database_schema: null,
      createdAt: now,
      updatedAt: now
    };

    // Add to configurations array
    const currentState = DatabaseStateService.getState();
    const updatedConfigurations = [...currentState.configurations, config];
    DatabaseStateService.setState({ configurations: updatedConfigurations });

    // Emit config added event
    configAdded$.next(config);

    return config;
  },

  /**
   * Create a new Snowflake database configuration using credentials
   */
  createSnowflakeConfig: (
    name: string,
    description: string,
    host: string,
    port: number,
    database: string,
    username: string,
    password: string,
    warehouse: string,
    account: string,
    role?: string
  ): IDatabaseConfig => {
    const id = uuidv4();
    const now = new Date().toISOString();

    const credentials: ISnowflakeCredentials = {
      id,
      name,
      description,
      type: DatabaseType.Snowflake,
      host,
      port,
      database,
      username,
      password,
      warehouse,
      account,
      role,
      createdAt: now,
      updatedAt: now
    };

    const config: IDatabaseConfig = {
      id,
      name,
      type: DatabaseType.Snowflake,
      connectionType: 'credentials',
      credentials,
      urlConnection: undefined,
      schema_last_updated: null,
      database_schema: null,
      createdAt: now,
      updatedAt: now
    };

    // Add to configurations array
    const currentState = DatabaseStateService.getState();
    const updatedConfigurations = [...currentState.configurations, config];
    DatabaseStateService.setState({ configurations: updatedConfigurations });

    // Emit config added event
    configAdded$.next(config);

    return config;
  },

  /**
   * Create a new database configuration using URL
   */
  createUrlConfig: (
    name: string,
    description: string,
    type: DatabaseType,
    connectionUrl: string
  ): IDatabaseConfig => {
    const id = uuidv4();
    const now = new Date().toISOString();

    const urlConnection: IDatabaseUrlConnection = {
      id,
      name,
      description,
      type,
      connectionUrl,
      createdAt: now,
      updatedAt: now
    };

    const config: IDatabaseConfig = {
      id,
      name,
      type,
      connectionType: 'url',
      credentials: undefined,
      urlConnection,
      schema_last_updated: null,
      database_schema: null,
      createdAt: now,
      updatedAt: now
    };

    // Add to configurations array
    const currentState = DatabaseStateService.getState();
    const updatedConfigurations = [...currentState.configurations, config];
    DatabaseStateService.setState({ configurations: updatedConfigurations });

    // Emit config added event
    configAdded$.next(config);

    return config;
  },

  /**
   * Get all database configurations
   */
  getConfigurations: (): IDatabaseConfig[] => {
    return DatabaseStateService.getState().configurations;
  },

  /**
   * Get a specific database configuration by ID
   */
  getConfiguration: (configId: string): IDatabaseConfig | null => {
    const configurations = DatabaseStateService.getState().configurations;
    return configurations.find(config => config.id === configId) || null;
  },

  /**
   * Update an existing database configuration
   */
  updateConfiguration: (
    configId: string,
    updates: Partial<IDatabaseConfig>
  ): boolean => {
    const currentState = DatabaseStateService.getState();
    const configIndex = currentState.configurations.findIndex(
      config => config.id === configId
    );

    if (configIndex === -1) {
      return false;
    }

    const updatedConfig = {
      ...currentState.configurations[configIndex],
      ...updates,
      updatedAt: new Date().toISOString()
    };

    const updatedConfigurations = [...currentState.configurations];
    updatedConfigurations[configIndex] = updatedConfig;

    DatabaseStateService.setState({ configurations: updatedConfigurations });

    // Update active config if it's the same
    if (currentState.activeConfigId === configId) {
      DatabaseStateService.setState({ activeConfig: updatedConfig });
    }

    // Emit config updated event
    configUpdated$.next(updatedConfig);

    return true;
  },

  /**
   * Remove a database configuration
   */
  removeConfiguration: (configId: string): boolean => {
    const currentState = DatabaseStateService.getState();
    const configIndex = currentState.configurations.findIndex(
      config => config.id === configId
    );

    if (configIndex === -1) {
      return false;
    }

    const configToRemove = currentState.configurations[configIndex];
    const updatedConfigurations = currentState.configurations.filter(
      config => config.id !== configId
    );

    DatabaseStateService.setState({ configurations: updatedConfigurations });

    // Clear active config if it was the removed one
    if (currentState.activeConfigId === configId) {
      DatabaseStateService.setState({
        activeConfigId: null,
        activeConfig: null
      });
    }

    // Emit config removed event
    configRemoved$.next({ configId, config: configToRemove });

    return true;
  },

  /**
   * Set the active database configuration
   */
  setActiveConfiguration: (configId: string | null): boolean => {
    const currentState = DatabaseStateService.getState();
    const oldConfigId = currentState.activeConfigId;

    if (configId === null) {
      DatabaseStateService.setState({
        activeConfigId: null,
        activeConfig: null
      });
      activeConfigChanged$.next({ oldConfigId, newConfigId: null });
      return true;
    }

    const config = DatabaseStateService.getConfiguration(configId);
    if (!config) {
      return false;
    }

    DatabaseStateService.setState({
      activeConfigId: configId,
      activeConfig: config
    });

    // Emit active config changed event
    activeConfigChanged$.next({ oldConfigId, newConfigId: configId });

    return true;
  },

  /**
   * Get the currently active configuration
   */
  getActiveConfiguration: (): IDatabaseConfig | null => {
    return DatabaseStateService.getState().activeConfig;
  },

  /**
   * Get configurations by database type
   */
  getConfigurationsByType: (type: DatabaseType): IDatabaseConfig[] => {
    return DatabaseStateService.getState().configurations.filter(
      config => config.type === type
    );
  },

  /**
   * Get configurations by connection type (credentials vs URL)
   */
  getConfigurationsByConnectionType: (
    connectionType: 'credentials' | 'url'
  ): IDatabaseConfig[] => {
    return DatabaseStateService.getState().configurations.filter(
      config => config.connectionType === connectionType
    );
  },

  // Event observables
  /**
   * Subscribe to configuration added events
   */
  onConfigurationAdded: (): Observable<IDatabaseConfig> => {
    return configAdded$.asObservable();
  },

  /**
   * Subscribe to configuration removed events
   */
  onConfigurationRemoved: (): Observable<{
    configId: string;
    config: IDatabaseConfig;
  }> => {
    return configRemoved$.asObservable();
  },

  /**
   * Subscribe to configuration updated events
   */
  onConfigurationUpdated: (): Observable<IDatabaseConfig> => {
    return configUpdated$.asObservable();
  },

  /**
   * Subscribe to active configuration change events
   */
  onActiveConfigurationChanged: (): Observable<{
    oldConfigId: string | null;
    newConfigId: string | null;
  }> => {
    return activeConfigChanged$.asObservable();
  },

  // Schema management methods

  /**
   * Fetch and update schema information for a database configuration
   * @param configId Database configuration ID
   * @returns Promise with schema fetch result
   */
  fetchAndUpdateSchema: async (
    configId: string
  ): Promise<{ success: boolean; error?: string; schema?: string }> => {
    try {
      const config = DatabaseStateService.getConfiguration(configId);
      if (!config) {
        return { success: false, error: 'Database configuration not found' };
      }

      // Build database URL from configuration
      let databaseUrl: string;

      if (config.connectionType === 'url' && config.urlConnection) {
        databaseUrl = config.urlConnection.connectionUrl;
      } else if (
        config.connectionType === 'credentials' &&
        config.credentials
      ) {
        const creds = config.credentials;
        // Build connection URL based on database type
        switch (config.type) {
          case DatabaseType.PostgreSQL:
            databaseUrl = `postgresql://${creds.username}:${creds.password}@${creds.host}:${creds.port}/${creds.database}`;
            break;
          case DatabaseType.MySQL:
            databaseUrl = `mysql://${creds.username}:${creds.password}@${creds.host}:${creds.port}/${creds.database}`;
            break;
          case DatabaseType.Snowflake:
            const sfCreds = creds as ISnowflakeCredentials;
            databaseUrl = `snowflake://${creds.username}:${creds.password}@${sfCreds.account}/${creds.database}?warehouse=${sfCreds.warehouse}${sfCreds.role ? `&role=${sfCreds.role}` : ''}`;
            break;
          default:
            return {
              success: false,
              error: 'Unsupported database type for schema fetching'
            };
        }
      } else {
        return { success: false, error: 'Invalid database configuration' };
      }

      // Create DatabaseTools instance and fetch schema
      const databaseTools = new DatabaseTools();
      const schemaResult = await databaseTools.getDatabaseMetadata(databaseUrl);

      // Parse the result
      let parsedResult;
      try {
        parsedResult = JSON.parse(schemaResult);
      } catch (parseError) {
        return {
          success: false,
          error: `Failed to parse schema result: ${parseError}`
        };
      }

      if (parsedResult.error) {
        return { success: false, error: parsedResult.error };
      }

      // Update the configuration with schema information
      const now = new Date().toISOString();
      const updateResult = DatabaseStateService.updateConfiguration(configId, {
        schema_last_updated: now,
        database_schema: parsedResult.schema_info || schemaResult
      });

      if (!updateResult) {
        return {
          success: false,
          error: 'Failed to update configuration with schema information'
        };
      }

      // Save to StateDB
      await DatabaseStateService.saveConfigurationsToStateDB();

      return {
        success: true,
        schema: parsedResult.schema_info || schemaResult
      };
    } catch (error) {
      console.error('[DatabaseStateService] Error fetching schema:', error);
      return {
        success: false,
        error: `Schema fetch failed: ${error instanceof Error ? error.message : String(error)}`
      };
    }
  },

  /**
   * Get schema information for a database configuration
   * @param configId Database configuration ID
   * @returns Schema information or null if not available
   */
  getSchemaInfo: (
    configId: string
  ): { lastUpdated: string | null; schema: string | null } | null => {
    const config = DatabaseStateService.getConfiguration(configId);
    if (!config) {
      return null;
    }

    return {
      lastUpdated: config.schema_last_updated || null,
      schema: config.database_schema || null
    };
  },

  /**
   * Check if schema information is available and fresh for a configuration
   * @param configId Database configuration ID
   * @param maxAgeHours Maximum age in hours before schema is considered stale (default: 24)
   * @returns True if schema is available and fresh
   */
  isSchemaFresh: (configId: string, maxAgeHours: number = 24): boolean => {
    const schemaInfo = DatabaseStateService.getSchemaInfo(configId);
    if (!schemaInfo || !schemaInfo.lastUpdated || !schemaInfo.schema) {
      return false;
    }

    const lastUpdated = new Date(schemaInfo.lastUpdated);
    const now = new Date();
    const ageHours = (now.getTime() - lastUpdated.getTime()) / (1000 * 60 * 60);

    return ageHours <= maxAgeHours;
  },

  // StateDB persistence methods with encoding

  /**
   * Save configurations to StateDB with encryption
   */
  saveConfigurationsToStateDB: async (): Promise<void> => {
    try {
      const state = DatabaseStateService.getState();

      if (state.configurations.length === 0) {
        console.log('[DatabaseStateService] No configurations to save');
        await StateDBCachingService.setObjectValue(
          'database_configurations',
          {}
        );
        return;
      }

      // Encode each configuration's sensitive data
      const encodedConfigs = state.configurations.map(config => {
        const encoded = { ...config };

        if (config.credentials) {
          // Encode the credentials
          encoded.credentials = {
            ...config.credentials,
            password: DatabaseEncoder.encode(config.credentials.password),
            username: DatabaseEncoder.encode(config.credentials.username)
          } as any;
        }

        if (config.urlConnection) {
          // Encode the connection URL
          encoded.urlConnection = {
            ...config.urlConnection,
            connectionUrl: DatabaseEncoder.encode(
              config.urlConnection.connectionUrl
            )
          };
        }

        return encoded;
      });

      await StateDBCachingService.setObjectValue(
        'database_configurations',
        encodedConfigs
      );
      console.log(
        '[DatabaseStateService] ✅ Configurations saved to StateDB with encoding'
      );
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to save configurations to StateDB:',
        error
      );
      throw error;
    }
  },

  /**
   * Load configurations from StateDB with decryption
   */
  loadConfigurationsFromStateDB: async (): Promise<void> => {
    try {
      const encodedConfigs = await StateDBCachingService.getObjectValue<
        IDatabaseConfig[]
      >('database_configurations', []);

      if (encodedConfigs.length === 0) {
        console.log(
          '[DatabaseStateService] No configurations found in StateDB'
        );
        return;
      }

      // Decode each configuration's sensitive data
      const decodedConfigs = encodedConfigs
        .map(config => {
          const decoded = { ...config };

          if (config.credentials) {
            try {
              decoded.credentials = {
                ...config.credentials,
                password: DatabaseEncoder.decode(config.credentials.password),
                username: DatabaseEncoder.decode(config.credentials.username)
              } as any;
            } catch (error) {
              console.warn(
                '[DatabaseStateService] Failed to decode credentials for config:',
                config.id,
                error
              );
              // Skip this config if decoding fails
              return null;
            }
          }

          if (config.urlConnection) {
            try {
              decoded.urlConnection = {
                ...config.urlConnection,
                connectionUrl: DatabaseEncoder.decode(
                  config.urlConnection.connectionUrl
                )
              };
            } catch (error) {
              console.warn(
                '[DatabaseStateService] Failed to decode URL connection for config:',
                config.id,
                error
              );
              // Skip this config if decoding fails
              return null;
            }
          }

          return decoded;
        })
        .filter(config => config !== null) as IDatabaseConfig[];

      // Update state
      DatabaseStateService.setState({ configurations: decodedConfigs });
      console.log(
        '[DatabaseStateService] ✅ Configurations loaded from StateDB with decoding'
      );
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to load configurations from StateDB:',
        error
      );
      throw error;
    }
  },

  /**
   * Create and persist a PostgreSQL configuration with encoding
   */
  createAndPersistPostgreSQLConfig: async (
    name: string,
    description: string,
    host: string,
    port: number,
    database: string,
    username: string,
    password: string
  ): Promise<IDatabaseConfig> => {
    try {
      // Create the configuration
      const config = DatabaseStateService.createPostgreSQLConfig(
        name,
        description,
        host,
        port,
        database,
        username,
        password
      );

      // Save to StateDB
      await DatabaseStateService.saveConfigurationsToStateDB();

      console.log(
        '[DatabaseStateService] ✅ PostgreSQL configuration created and persisted'
      );
      return config;
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to create and persist PostgreSQL config:',
        error
      );
      throw error;
    }
  },

  /**
   * Create and persist a Snowflake configuration with encoding
   */
  createAndPersistSnowflakeConfig: async (
    name: string,
    description: string,
    host: string,
    port: number,
    database: string,
    username: string,
    password: string,
    warehouse: string,
    account: string,
    role?: string
  ): Promise<IDatabaseConfig> => {
    try {
      // Create the configuration
      const config = DatabaseStateService.createSnowflakeConfig(
        name,
        description,
        host,
        port,
        database,
        username,
        password,
        warehouse,
        account,
        role
      );

      // Save to StateDB
      await DatabaseStateService.saveConfigurationsToStateDB();

      console.log(
        '[DatabaseStateService] ✅ Snowflake configuration created and persisted'
      );
      return config;
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to create and persist Snowflake config:',
        error
      );
      throw error;
    }
  },

  /**
   * Create and persist a MySQL configuration with encoding
   */
  createAndPersistMySQLConfig: async (
    name: string,
    description: string,
    host: string,
    port: number,
    database: string,
    username: string,
    password: string
  ): Promise<IDatabaseConfig> => {
    try {
      // Create the configuration
      const config = DatabaseStateService.createMySQLConfig(
        name,
        description,
        host,
        port,
        database,
        username,
        password
      );

      // Save to StateDB
      await DatabaseStateService.saveConfigurationsToStateDB();

      console.log(
        '[DatabaseStateService] ✅ MySQL configuration created and persisted'
      );
      return config;
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to create and persist MySQL config:',
        error
      );
      throw error;
    }
  },

  /**
   * Remove configuration and update StateDB
   */
  removeConfigurationAndPersist: async (configId: string): Promise<boolean> => {
    try {
      const removed = DatabaseStateService.removeConfiguration(configId);

      if (removed) {
        await DatabaseStateService.saveConfigurationsToStateDB();
        console.log(
          '[DatabaseStateService] ✅ Configuration removed and persisted'
        );
      }

      return removed;
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to remove and persist configuration:',
        error
      );
      throw error;
    }
  },

  /**
   * Update and persist a database configuration
   */
  updateConfigurationAndPersist: async (
    configId: string,
    updates: Partial<IDatabaseConfig>
  ): Promise<boolean> => {
    try {
      const updated = DatabaseStateService.updateConfiguration(
        configId,
        updates
      );

      if (updated) {
        await DatabaseStateService.saveConfigurationsToStateDB();
        console.log(
          '[DatabaseStateService] ✅ Configuration updated and persisted'
        );
      }

      return updated;
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to update and persist configuration:',
        error
      );
      throw error;
    }
  },

  /**
   * Update a database configuration from form data and persist
   */
  updateConfigurationFromFormDataAndPersist: async (
    configId: string,
    name: string,
    description: string,
    type: DatabaseType,
    connectionMethod: 'credentials' | 'url',
    host?: string,
    port?: number,
    database?: string,
    username?: string,
    password?: string,
    connectionUrl?: string,
    warehouse?: string,
    account?: string,
    role?: string
  ): Promise<boolean> => {
    try {
      const currentConfig = DatabaseStateService.getConfiguration(configId);
      if (!currentConfig) {
        return false;
      }

      // Prepare the updated configuration
      const updatedAt = new Date().toISOString();

      let updatedConfig: IDatabaseConfig;

      if (connectionMethod === 'url' && connectionUrl) {
        // URL-based configuration
        updatedConfig = {
          ...currentConfig,
          name,
          type,
          connectionType: 'url',
          credentials: undefined,
          urlConnection: {
            id: currentConfig.id,
            name,
            description,
            type,
            connectionUrl,
            createdAt: currentConfig.createdAt,
            updatedAt
          },
          updatedAt
        };
      } else {
        // Credentials-based configuration
        let credentials:
          | IMySQLCredentials
          | IPostgreSQLCredentials
          | ISnowflakeCredentials;

        const baseCredentials = {
          id: currentConfig.id,
          name,
          description,
          type,
          host: host!,
          port: port!,
          database: database!,
          username: username!,
          password: password!,
          createdAt: currentConfig.createdAt,
          updatedAt
        };

        if (type === DatabaseType.Snowflake) {
          credentials = {
            ...baseCredentials,
            type: DatabaseType.Snowflake,
            warehouse: warehouse!,
            account: account!,
            role: role || undefined
          } as ISnowflakeCredentials;
        } else if (type === DatabaseType.MySQL) {
          credentials = {
            ...baseCredentials,
            type: DatabaseType.MySQL
          } as IMySQLCredentials;
        } else {
          credentials = {
            ...baseCredentials,
            type: DatabaseType.PostgreSQL
          } as IPostgreSQLCredentials;
        }

        updatedConfig = {
          ...currentConfig,
          name,
          type,
          connectionType: 'credentials',
          credentials,
          urlConnection: undefined,
          updatedAt
        };
      }

      // Update and persist
      const updated = DatabaseStateService.updateConfiguration(
        configId,
        updatedConfig
      );

      if (updated) {
        await DatabaseStateService.saveConfigurationsToStateDB();
        console.log(
          '[DatabaseStateService] ✅ Configuration updated from form data and persisted'
        );
      }

      return updated;
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to update configuration from form data:',
        error
      );
      throw error;
    }
  },

  /**
   * Initialize service and load configurations from StateDB
   */
  initializeWithStateDB: async (): Promise<void> => {
    try {
      DatabaseStateService.initialize();
      await DatabaseStateService.loadConfigurationsFromStateDB();
      console.log(
        '[DatabaseStateService] ✅ Service initialized with StateDB data'
      );
    } catch (error) {
      console.error(
        '[DatabaseStateService] ❌ Failed to initialize with StateDB:',
        error
      );
      // Continue initialization even if loading fails
      DatabaseStateService.initialize();
    }
  }
};
