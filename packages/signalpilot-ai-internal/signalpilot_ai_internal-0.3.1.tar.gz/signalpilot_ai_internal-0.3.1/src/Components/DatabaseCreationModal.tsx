import * as React from 'react';
import { Modal, Button, Form, Alert } from 'react-bootstrap';
import {
  DatabaseType,
  IDatabaseConfig,
  DatabaseStateService
} from '../DatabaseStateService';

/**
 * Props for the DatabaseCreationModal component
 */
export interface DatabaseCreationModalProps {
  isVisible: boolean;
  onClose: () => void;
  onCreateDatabase: (dbConfig: DatabaseFormData) => Promise<void>;
  onValidateSchema?: (
    dbConfig: DatabaseFormData
  ) => Promise<{ success: boolean; error?: string; schema?: string }>;
  editConfig?: IDatabaseConfig; // Optional config to edit
  initialType?: DatabaseType; // Optional initial database type to pre-select
}

/**
 * Connection method type
 */
export type ConnectionMethod = 'url' | 'config';

/**
 * Database form data interface
 */
export interface DatabaseFormData {
  id?: string; // Include ID for updates
  name: string;
  description: string;
  type: DatabaseType;
  connectionMethod: ConnectionMethod;
  connectionUrl: string;
  host: string;
  port: number;
  database: string;
  username: string;
  password: string;
  // Snowflake-specific fields
  warehouse: string;
  account: string;
  role: string;
  // Schema information (populated after successful validation)
  schema?: string;
  schemaLastUpdated?: string;
}

/**
 * Database creation modal component for adding database configurations
 */
export function DatabaseCreationModal({
  isVisible,
  onClose,
  onCreateDatabase,
  onValidateSchema,
  editConfig,
  initialType
}: DatabaseCreationModalProps): JSX.Element | null {
  const [formData, setFormData] = React.useState<DatabaseFormData>({
    name: '',
    description: '',
    type: DatabaseType.PostgreSQL,
    connectionMethod: 'config',
    connectionUrl: '',
    host: 'localhost',
    port: 5432,
    database: '',
    username: '',
    password: '',
    warehouse: '',
    account: '',
    role: '',
    schema: undefined,
    schemaLastUpdated: undefined
  });

  const [isSubmitting, setIsSubmitting] = React.useState(false);
  const [isCheckingSchema, setIsCheckingSchema] = React.useState(false);
  const [errors, setErrors] = React.useState<Partial<DatabaseFormData>>({});
  const [databaseError, setDatabaseError] = React.useState<string>('');
  const [duplicateNameWarning, setDuplicateNameWarning] =
    React.useState<string>('');
  const [schemaError, setSchemaError] = React.useState<{
    show: boolean;
    message: string;
    formData?: DatabaseFormData;
  }>({ show: false, message: '' });

  // Helper function to get default form data
  const getDefaultFormData = (dbType?: DatabaseType): DatabaseFormData => {
    const type = dbType || DatabaseType.PostgreSQL;
    const defaultPorts = {
      [DatabaseType.PostgreSQL]: 5432,
      [DatabaseType.MySQL]: 3306,
      [DatabaseType.Snowflake]: 443
    };

    return {
      name: '',
      description: '',
      type: type,
      connectionMethod: 'config',
      connectionUrl: '',
      host: 'localhost',
      port: defaultPorts[type] || 5432,
      database: '',
      username: '',
      password: '',
      warehouse: '',
      account: '',
      role: '',
      schema: undefined,
      schemaLastUpdated: undefined
    };
  };

  // Helper function to convert database config to form data for editing
  const configToFormData = (config: IDatabaseConfig): DatabaseFormData => {
    const baseData: DatabaseFormData = {
      id: config.id, // Include ID for updates
      name: config.name,
      description:
        config.credentials?.description ||
        config.urlConnection?.description ||
        '',
      type: config.type,
      connectionMethod:
        config.connectionType === 'credentials' ? 'config' : 'url',
      connectionUrl: config.urlConnection?.connectionUrl || '',
      host: config.credentials?.host || 'localhost',
      port: config.credentials?.port || 5432,
      database:
        config.credentials?.database || config.urlConnection?.name || '',
      username: config.credentials?.username || '',
      password: config.credentials?.password || '',
      warehouse: '',
      account: '',
      role: '',
      // Include existing schema information
      schema: config.database_schema || undefined,
      schemaLastUpdated: config.schema_last_updated || undefined
    };

    // Handle Snowflake-specific fields
    if (
      config.type === DatabaseType.Snowflake &&
      config.credentials &&
      'warehouse' in config.credentials
    ) {
      const snowflakeCredentials = config.credentials as any;
      baseData.warehouse = snowflakeCredentials.warehouse || '';
      baseData.account = snowflakeCredentials.account || '';
      baseData.role = snowflakeCredentials.role || '';
    }

    return baseData;
  };

  // Initialize form data - either default or from edit config
  const getInitialFormData = (): DatabaseFormData => {
    if (editConfig) {
      return configToFormData(editConfig);
    }
    return getDefaultFormData();
  };

  // Reset form when modal closes or when editConfig changes
  React.useEffect(() => {
    if (!isVisible) {
      setFormData(getDefaultFormData());
      setErrors({});
      setDatabaseError('');
      setDuplicateNameWarning('');
      setIsSubmitting(false);
      setIsCheckingSchema(false);
      setSchemaError({ show: false, message: '' });
    } else if (editConfig) {
      // Modal is opening with edit config
      setFormData(configToFormData(editConfig));
      setErrors({});
      setDatabaseError('');
      setDuplicateNameWarning('');
      setIsSubmitting(false);
      setIsCheckingSchema(false);
      setSchemaError({ show: false, message: '' });
    } else {
      // Modal is opening for new creation - use initialType if provided
      setFormData(getDefaultFormData(initialType));
      setErrors({});
      setDatabaseError('');
      setDuplicateNameWarning('');
      setIsSubmitting(false);
      setIsCheckingSchema(false);
      setSchemaError({ show: false, message: '' });
    }
  }, [isVisible, editConfig, initialType]);

  // Update default port when database type changes
  React.useEffect(() => {
    const defaultPorts = {
      [DatabaseType.PostgreSQL]: 5432,
      [DatabaseType.MySQL]: 3306,
      [DatabaseType.Snowflake]: 443
    };

    setFormData(prev => ({
      ...prev,
      port: defaultPorts[prev.type] || 5432,
      // Force config method for Snowflake since it doesn't support URL connections
      connectionMethod:
        prev.type === DatabaseType.Snowflake ? 'config' : prev.connectionMethod
    }));
  }, [formData.type]);

  const handleInputChange = (
    field: keyof DatabaseFormData,
    value: string | number | DatabaseType
  ) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));

    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => {
        const newErrors = { ...prev };
        delete newErrors[field];
        return newErrors;
      });
    }

    // Clear database error when user modifies form
    if (databaseError) {
      setDatabaseError('');
    }

    // Clear duplicate name warning when user modifies name field
    if (field === 'name' && duplicateNameWarning) {
      setDuplicateNameWarning('');
    }

    // Run duplicate name validation in real-time for name field
    if (field === 'name' && typeof value === 'string') {
      const trimmedName = value.trim();
      if (trimmedName) {
        const existingConfigs = DatabaseStateService.getConfigurations();
        const duplicateConfig = existingConfigs.find(
          config =>
            config.name.toLowerCase() === trimmedName.toLowerCase() &&
            config.id !== formData.id // Exclude current config when editing
        );

        if (duplicateConfig) {
          setDuplicateNameWarning(
            `A database with the name "${trimmedName}" already exists. Database names must be unique.`
          );
        }
      }
    }
  };

  const parseConnectionUrl = (url: string) => {
    try {
      const urlObj = new URL(url);

      // Get default port based on protocol
      let defaultPort = 5432; // PostgreSQL default
      if (urlObj.protocol === 'mysql:') {
        defaultPort = 3306;
      }

      return {
        host: urlObj.hostname,
        port: parseInt(urlObj.port) || defaultPort,
        database: urlObj.pathname.slice(1) || '',
        username: urlObj.username,
        password: urlObj.password
      };
    } catch {
      return null;
    }
  };

  const validateForm = (): boolean => {
    const newErrors: Partial<DatabaseFormData> = {};

    // Common validation
    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    } else {
      // Check for duplicate names
      const existingConfigs = DatabaseStateService.getConfigurations();
      const duplicateConfig = existingConfigs.find(
        config =>
          config.name.toLowerCase() === formData.name.trim().toLowerCase() &&
          config.id !== formData.id // Exclude current config when editing
      );

      if (duplicateConfig) {
        setDuplicateNameWarning(
          `A database with the name "${formData.name.trim()}" already exists. Database names must be unique.`
        );
      } else {
        setDuplicateNameWarning('');
      }
    }

    if (formData.connectionMethod === 'url') {
      // URL-based validation
      if (!formData.connectionUrl.trim()) {
        newErrors.connectionUrl = 'Connection URL is required' as any;
      } else {
        const parsed = parseConnectionUrl(formData.connectionUrl);
        if (!parsed) {
          newErrors.connectionUrl = 'Invalid connection URL format' as any;
        } else {
          if (!parsed.host) {
            newErrors.connectionUrl =
              'Host is required in connection URL' as any;
          }
          if (!parsed.database) {
            newErrors.connectionUrl =
              'Database name is required in connection URL' as any;
          }
          if (!parsed.username) {
            newErrors.connectionUrl =
              'Username is required in connection URL' as any;
          }
          if (!parsed.password) {
            newErrors.connectionUrl =
              'Password is required in connection URL' as any;
          }
        }
      }
    } else {
      // Config-based validation
      if (!formData.host.trim()) {
        newErrors.host = 'Host is required';
      }

      if (!formData.database.trim()) {
        newErrors.database = 'Database name is required';
      }

      if (!formData.username.trim()) {
        newErrors.username = 'Username is required';
      }

      if (!formData.password.trim()) {
        newErrors.password = 'Password is required';
      }

      if (formData.port <= 0 || formData.port > 65535) {
        newErrors.port = 'Port must be between 1 and 65535' as any;
      }

      // Snowflake-specific validation
      if (formData.type === DatabaseType.Snowflake) {
        if (!formData.account.trim()) {
          newErrors.account = 'Account identifier is required' as any;
        }

        if (!formData.warehouse.trim()) {
          newErrors.warehouse = 'Warehouse is required' as any;
        }
      }
    }

    setErrors(newErrors);

    // Also check if there's a duplicate name warning - this should prevent submission
    const hasValidationErrors =
      Object.keys(newErrors).length > 0 || duplicateNameWarning !== '';
    return !hasValidationErrors;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setDatabaseError(''); // Clear previous database errors

    let submitData = { ...formData };

    try {
      // If using URL method, parse URL and populate individual fields
      if (formData.connectionMethod === 'url') {
        const parsed = parseConnectionUrl(formData.connectionUrl);
        if (parsed) {
          submitData = {
            ...submitData,
            host: parsed.host,
            port: parsed.port,
            database: parsed.database,
            username: parsed.username,
            password: parsed.password
          };
        }
      }

      // Validate schema FIRST (for both new connections and updates)
      if (onValidateSchema) {
        setIsCheckingSchema(true);

        try {
          const schemaResult = await onValidateSchema(submitData);

          if (!schemaResult.success) {
            // Show schema error modal
            setSchemaError({
              show: true,
              message: schemaResult.error || 'Unknown schema validation error',
              formData: submitData
            });
            setIsCheckingSchema(false);
            return;
          }

          // Schema validation succeeded, store schema information and continue to create/update database
          if (schemaResult.schema) {
            submitData.schema = schemaResult.schema;
            submitData.schemaLastUpdated = new Date().toISOString();
          }
          setIsCheckingSchema(false);
        } catch (schemaValidationError) {
          // Show schema error modal for connection errors during schema loading
          const errorMessage =
            schemaValidationError instanceof Error
              ? schemaValidationError.message
              : String(schemaValidationError);
          setSchemaError({
            show: true,
            message: `Database connection failed: ${errorMessage}`,
            formData: submitData
          });
          setIsCheckingSchema(false);
          return;
        }
      }

      // Now create/update the database (only after schema validation passes)
      setIsSubmitting(true);

      try {
        await onCreateDatabase(submitData);
        // Only close if everything succeeded
        onClose();
      } catch (dbError) {
        // Database creation/update failed - show error modal
        const errorMessage =
          dbError instanceof Error ? dbError.message : String(dbError);
        setSchemaError({
          show: true,
          message: `Database ${editConfig ? 'update' : 'creation'} failed: ${errorMessage}`,
          formData: submitData
        });
        return; // Don't close modal
      }
    } catch (error) {
      console.error('[DatabaseCreationModal] Unexpected error:', error);
      const errorMessage =
        error instanceof Error ? error.message : String(error);
      setSchemaError({
        show: true,
        message: `Unexpected error: ${errorMessage}`,
        formData: submitData
      });
    } finally {
      setIsSubmitting(false);
      setIsCheckingSchema(false);
    }
  };

  const handleClose = () => {
    if (!isSubmitting && !isCheckingSchema) {
      onClose();
    }
  };

  // Schema error modal handlers
  const handleSchemaRetry = async () => {
    if (!schemaError.formData) return;

    // Clear the error state and go back to the original modal view
    setSchemaError({ show: false, message: '' });

    // Set the form data back to what was being submitted
    setFormData(schemaError.formData);

    // Redo the "Loading Schema" state - this follows the same flow as handleSubmit
    if (onValidateSchema) {
      setIsCheckingSchema(true);

      try {
        const schemaResult = await onValidateSchema(schemaError.formData);

        if (!schemaResult.success) {
          // Show schema error modal again
          setSchemaError({
            show: true,
            message: schemaResult.error || 'Unknown schema validation error',
            formData: schemaError.formData
          });
          setIsCheckingSchema(false);
          return;
        }

        // Schema validation succeeded, store schema information and continue to create/update database
        if (schemaResult.schema) {
          schemaError.formData.schema = schemaResult.schema;
          schemaError.formData.schemaLastUpdated = new Date().toISOString();
        }
        setIsCheckingSchema(false);
        setIsSubmitting(true);

        try {
          await onCreateDatabase(schemaError.formData);
          // Success! Close the modal
          onClose();
        } catch (dbError) {
          const errorMessage =
            dbError instanceof Error ? dbError.message : String(dbError);
          setSchemaError({
            show: true,
            message: `Database ${editConfig ? 'update' : 'creation'} failed: ${errorMessage}`,
            formData: schemaError.formData
          });
          setIsSubmitting(false);
        }
      } catch (schemaValidationError) {
        // Show schema error modal for connection errors during schema loading
        const errorMessage =
          schemaValidationError instanceof Error
            ? schemaValidationError.message
            : String(schemaValidationError);
        setSchemaError({
          show: true,
          message: `Database connection failed: ${errorMessage}`,
          formData: schemaError.formData
        });
        setIsCheckingSchema(false);
      }
    }
  };

  const handleSchemaEdit = () => {
    // Close schema error modal and return to editing
    setSchemaError({ show: false, message: '' });
  };

  const handleSaveWithoutSchema = async () => {
    if (!schemaError.formData) return;

    // User explicitly wants to save without schema validation
    setSchemaError({ show: false, message: '' });
    setIsSubmitting(true);
    setDatabaseError(''); // Clear any previous errors

    try {
      await onCreateDatabase(schemaError.formData);
      // Successfully saved, close the modal
      onClose();
    } catch (dbError) {
      // Database creation/update failed - show error
      const errorMessage =
        dbError instanceof Error ? dbError.message : String(dbError);
      setDatabaseError(
        `Database ${editConfig ? 'update' : 'creation'} failed: ${errorMessage}`
      );
      setSchemaError({
        show: true,
        message: `Database ${editConfig ? 'update' : 'creation'} failed: ${errorMessage}`,
        formData: schemaError.formData
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!isVisible) {
    return null;
  }

  const getDatabaseIcon = (type: DatabaseType) => {
    switch (type) {
      case DatabaseType.PostgreSQL:
        return '🐘';
      case DatabaseType.MySQL:
        return '🐬';
      case DatabaseType.Snowflake:
        return '❄️';
      default:
        return '🗃️';
    }
  };

  return (
    <Modal
      show={isVisible}
      onHide={handleClose}
      backdrop={isSubmitting || isCheckingSchema ? 'static' : true}
      keyboard={!isSubmitting && !isCheckingSchema}
      centered
      dialogClassName="sage-ai-database-creation-modal"
      size="lg"
      scrollable={true}
    >
      <Modal.Header closeButton={!isSubmitting} className="modal-header-modern">
        <div className="modal-title-section">
          <div className="modal-icon">
            <span className="icon-database">🗄️</span>
          </div>
          <div className="modal-title-text">
            <Modal.Title className="sage-ai-database-modal-title">
              {editConfig
                ? 'Edit Database Connection'
                : 'Add Database Connection'}
            </Modal.Title>
            <p className="modal-subtitle">
              {editConfig
                ? 'Update your database connection settings'
                : 'Connect to your database securely'}
            </p>
          </div>
        </div>
      </Modal.Header>

      <Modal.Body className="sage-ai-database-modal-body">
        {schemaError.show ? (
          // Error display content
          <>
            {/* Error Details */}
            <Alert variant="danger" className="mb-4">
              <Alert.Heading className="h6 mb-2">
                <span className="me-2">🚨</span>
                Connection Error Details
              </Alert.Heading>
              <div className="error-message-container">
                <code className="text-danger">{schemaError.message}</code>
              </div>
            </Alert>

            {/* Warning Message */}
            <Alert variant="warning" className="mb-4">
              <Alert.Heading className="h6 mb-2">
                <span className="me-2">⚠️</span>
                Important Notice
              </Alert.Heading>
              <p className="mb-0">
                <strong>
                  If you continue without schema information, SignalPilot will
                  have significantly reduced accuracy when answering questions
                  about your database.
                </strong>
              </p>
              <p className="mb-0 mt-2 text-muted small">
                Schema information helps SignalPilot understand your database
                structure, table relationships, and column types for more
                accurate query generation and data analysis.
              </p>
            </Alert>

            {/* Action Options */}
            <div className="action-options">
              <h6 className="mb-3">What would you like to do?</h6>

              <div className="option-cards">
                <button
                  className="option-card recommended"
                  onClick={handleSchemaRetry}
                  disabled={isCheckingSchema}
                  type="button"
                >
                  <div className="option-icon">🔄</div>
                  <div className="option-content">
                    <div className="option-title">
                      {isCheckingSchema ? 'Retrying...' : 'Retry Schema Fetch'}
                    </div>
                    <div className="option-description">
                      Try connecting to the database again to retrieve schema
                      information
                    </div>
                  </div>
                  <div className="option-badge">Recommended</div>
                </button>

                <button
                  className="option-card"
                  onClick={handleSchemaEdit}
                  disabled={isCheckingSchema}
                  type="button"
                >
                  <div className="option-icon">✏️</div>
                  <div className="option-content">
                    <div className="option-title">Edit Connection Settings</div>
                    <div className="option-description">
                      Modify database connection parameters and try again
                    </div>
                  </div>
                </button>

                <button
                  className="option-card warning"
                  onClick={handleSaveWithoutSchema}
                  disabled={isCheckingSchema}
                  type="button"
                >
                  <div className="option-icon">⚠️</div>
                  <div className="option-content">
                    <div className="option-title">Continue Without Schema</div>
                    <div className="option-description">
                      Save the connection but with limited AI accuracy
                    </div>
                  </div>
                  <div className="option-badge warning">Limited Accuracy</div>
                </button>
              </div>
            </div>
          </>
        ) : (
          // Form content (existing form)
          <Form onSubmit={handleSubmit}>
            {/* Database Error Alert */}
            {databaseError && (
              <div
                className="alert alert-danger d-flex align-items-center mb-3"
                role="alert"
              >
                <div className="alert-icon me-2">⚠️</div>
                <div className="flex-grow-1">
                  <strong>Connection Failed</strong>
                  <div className="mt-1 small">{databaseError}</div>
                </div>
                <button
                  type="button"
                  className="btn-close"
                  aria-label="Close"
                  onClick={() => setDatabaseError('')}
                ></button>
              </div>
            )}
            {/* Duplicate Name Warning */}
            {duplicateNameWarning && (
              <div
                className="alert alert-danger d-flex align-items-center mb-3"
                role="alert"
              >
                <div className="alert-icon me-2" style={{ color: '#dc3545' }}>
                  🚨
                </div>
                <div className="flex-grow-1">
                  <strong>Duplicate Name Warning</strong>
                  <div className="mt-1 small">{duplicateNameWarning}</div>
                </div>
              </div>
            )}
            {/* Connection Info Section */}
            <div className="form-section-compact">
              {/* Connection Name */}
              <div className="form-row-compact">
                <label htmlFor="connectionName" className="form-label-inline">
                  Connection Name <span className="text-danger">*</span>
                </label>
                <div className="form-input-wrapper">
                  <Form.Control
                    id="connectionName"
                    type="text"
                    value={formData.name}
                    onChange={e => handleInputChange('name', e.target.value)}
                    isInvalid={!!errors.name}
                    placeholder="e.g., Production DB, Analytics DB"
                    disabled={isSubmitting}
                    className="form-control-compact"
                    autoComplete="off"
                    data-form-type="other"
                    spellCheck={false}
                  />
                  {errors.name && (
                    <div className="invalid-feedback-inline">{errors.name}</div>
                  )}
                </div>
              </div>

              {/* Description */}
              <div className="form-row-compact">
                <label
                  htmlFor="connectionDescription"
                  className="form-label-inline"
                >
                  Description
                </label>
                <div className="form-input-wrapper">
                  <Form.Control
                    id="connectionDescription"
                    as="textarea"
                    rows={2}
                    value={formData.description}
                    onChange={e =>
                      handleInputChange('description', e.target.value)
                    }
                    placeholder="Optional description"
                    disabled={isSubmitting}
                    className="form-control-compact"
                    autoComplete="off"
                    data-form-type="other"
                    spellCheck={false}
                  />
                </div>
              </div>

              {/* Database Type */}
              <div className="form-row-compact">
                <label className="form-label-inline">
                  Database Type <span className="text-danger">*</span>
                </label>
                <div className="form-input-wrapper">
                  <div className="database-type-buttons-compact">
                    <button
                      type="button"
                      className={`db-type-btn-compact ${formData.type === DatabaseType.PostgreSQL ? 'selected' : ''}`}
                      onClick={() =>
                        !isSubmitting &&
                        handleInputChange('type', DatabaseType.PostgreSQL)
                      }
                      disabled={isSubmitting}
                    >
                      <span className="db-icon-small">
                        {getDatabaseIcon(DatabaseType.PostgreSQL)}
                      </span>
                      PostgreSQL
                    </button>
                    <button
                      type="button"
                      className={`db-type-btn-compact ${formData.type === DatabaseType.MySQL ? 'selected' : ''}`}
                      onClick={() =>
                        !isSubmitting &&
                        handleInputChange('type', DatabaseType.MySQL)
                      }
                      disabled={isSubmitting}
                    >
                      <span className="db-icon-small">
                        {getDatabaseIcon(DatabaseType.MySQL)}
                      </span>
                      MySQL
                    </button>
                    <button
                      type="button"
                      className={`db-type-btn-compact ${formData.type === DatabaseType.Snowflake ? 'selected' : ''}`}
                      onClick={() =>
                        !isSubmitting &&
                        handleInputChange('type', DatabaseType.Snowflake)
                      }
                      disabled={isSubmitting}
                    >
                      <span className="db-icon-small">
                        {getDatabaseIcon(DatabaseType.Snowflake)}
                      </span>
                      Snowflake
                    </button>
                  </div>
                </div>
              </div>

              {/* Connection Method */}
              <div className="form-row-compact">
                <label className="form-label-inline">
                  Connection Method <span className="text-danger">*</span>
                </label>
                <div className="form-input-wrapper">
                  <div className="connection-method-buttons-compact">
                    <button
                      type="button"
                      className={`method-btn-compact ${formData.connectionMethod === 'url' ? 'selected' : ''}`}
                      onClick={() =>
                        !isSubmitting &&
                        formData.type !== DatabaseType.Snowflake &&
                        handleInputChange('connectionMethod', 'url')
                      }
                      disabled={
                        isSubmitting || formData.type === DatabaseType.Snowflake
                      }
                    >
                      🔗 Connection URL
                    </button>
                    <button
                      type="button"
                      className={`method-btn-compact ${formData.connectionMethod === 'config' ? 'selected' : ''}`}
                      onClick={() =>
                        !isSubmitting &&
                        handleInputChange('connectionMethod', 'config')
                      }
                      disabled={isSubmitting}
                    >
                      ⚙️ Configuration
                    </button>
                  </div>
                  {formData.type === DatabaseType.Snowflake &&
                    formData.connectionMethod === 'url' && (
                      <div className="text-muted small mt-1">
                        Snowflake requires configuration method
                      </div>
                    )}
                </div>
              </div>
            </div>
            {/* Connection URL Section */}
            {formData.connectionMethod === 'url' && (
              <div className="form-section-compact">
                <div className="form-row-compact">
                  <label htmlFor="connectionUrl" className="form-label-inline">
                    Connection URL <span className="text-danger">*</span>
                  </label>
                  <div className="form-input-wrapper">
                    <Form.Control
                      id="connectionUrl"
                      type="text"
                      value={formData.connectionUrl}
                      onChange={e =>
                        handleInputChange('connectionUrl', e.target.value)
                      }
                      isInvalid={!!errors.connectionUrl}
                      placeholder={
                        formData.type === DatabaseType.MySQL
                          ? 'mysql://username:password@host:port/database'
                          : 'postgresql://username:password@host:port/database'
                      }
                      disabled={isSubmitting}
                      className="form-control-compact"
                      autoComplete="off"
                      data-form-type="other"
                      spellCheck={false}
                    />
                    {errors.connectionUrl && (
                      <div className="invalid-feedback-inline">
                        {errors.connectionUrl}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            )}
            {/* Server Configuration Section */}
            {formData.connectionMethod === 'config' && (
              <>
                <div className="form-section-compact">
                  {/* Host and Port */}
                  <div className="form-row-compact form-row-compact-reduced">
                    <label htmlFor="host" className="form-label-inline">
                      Host <span className="text-danger">*</span>
                    </label>
                    <div className="form-input-wrapper">
                      <div className="input-group-compact">
                        <Form.Control
                          id="host"
                          type="text"
                          value={formData.host}
                          onChange={e =>
                            handleInputChange('host', e.target.value)
                          }
                          isInvalid={!!errors.host}
                          placeholder="localhost or db.example.com"
                          disabled={isSubmitting}
                          className="form-control-compact flex-grow-1"
                          autoComplete="off"
                          data-form-type="other"
                          spellCheck={false}
                        />
                        <Form.Control
                          id="port"
                          type="number"
                          value={formData.port}
                          onChange={e =>
                            handleInputChange('port', parseInt(e.target.value))
                          }
                          isInvalid={!!errors.port}
                          min="1"
                          max="65535"
                          disabled={isSubmitting}
                          className="form-control-compact port-input"
                          autoComplete="off"
                          data-form-type="other"
                          placeholder="Port"
                        />
                      </div>
                      {(errors.host || errors.port) && (
                        <div className="invalid-feedback-inline">
                          {errors.host || String(errors.port || '')}
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Database */}
                  <div className="form-row-compact form-row-compact-reduced">
                    <label htmlFor="database" className="form-label-inline">
                      Database <span className="text-danger">*</span>
                    </label>
                    <div className="form-input-wrapper">
                      <Form.Control
                        id="database"
                        type="text"
                        value={formData.database}
                        onChange={e =>
                          handleInputChange('database', e.target.value)
                        }
                        isInvalid={!!errors.database}
                        placeholder="Database name"
                        disabled={isSubmitting}
                        className="form-control-compact"
                        autoComplete="off"
                        data-form-type="other"
                        spellCheck={false}
                      />
                      {errors.database && (
                        <div className="invalid-feedback-inline">
                          {errors.database}
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Snowflake-specific fields */}
                  {formData.type === DatabaseType.Snowflake && (
                    <>
                      <div className="form-row-compact">
                        <label htmlFor="account" className="form-label-inline">
                          Account <span className="text-danger">*</span>
                        </label>
                        <div className="form-input-wrapper">
                          <Form.Control
                            id="account"
                            type="text"
                            value={formData.account}
                            onChange={e =>
                              handleInputChange('account', e.target.value)
                            }
                            isInvalid={!!errors.account}
                            placeholder="your-account.snowflakecomputing.com"
                            disabled={isSubmitting}
                            className="form-control-compact"
                            autoComplete="off"
                            data-form-type="other"
                            spellCheck={false}
                          />
                          {errors.account && (
                            <div className="invalid-feedback-inline">
                              {errors.account}
                            </div>
                          )}
                        </div>
                      </div>

                      <div className="form-row-compact">
                        <label
                          htmlFor="warehouse"
                          className="form-label-inline"
                        >
                          Warehouse <span className="text-danger">*</span>
                        </label>
                        <div className="form-input-wrapper">
                          <Form.Control
                            id="warehouse"
                            type="text"
                            value={formData.warehouse}
                            onChange={e =>
                              handleInputChange('warehouse', e.target.value)
                            }
                            isInvalid={!!errors.warehouse}
                            placeholder="Warehouse name"
                            disabled={isSubmitting}
                            className="form-control-compact"
                            autoComplete="off"
                            data-form-type="other"
                            spellCheck={false}
                          />
                          {errors.warehouse && (
                            <div className="invalid-feedback-inline">
                              {errors.warehouse}
                            </div>
                          )}
                        </div>
                      </div>

                      <div className="form-row-compact">
                        <label htmlFor="role" className="form-label-inline">
                          Role
                        </label>
                        <div className="form-input-wrapper">
                          <Form.Control
                            id="role"
                            type="text"
                            value={formData.role}
                            onChange={e =>
                              handleInputChange('role', e.target.value)
                            }
                            placeholder="Optional role name"
                            disabled={isSubmitting}
                            className="form-control-compact"
                            autoComplete="off"
                            data-form-type="other"
                            spellCheck={false}
                          />
                        </div>
                      </div>
                    </>
                  )}

                  {/* Username */}
                  <div className="form-row-compact form-row-compact-reduced">
                    <label htmlFor="username" className="form-label-inline">
                      Username <span className="text-danger">*</span>
                    </label>
                    <div className="form-input-wrapper">
                      <Form.Control
                        id="username"
                        type="text"
                        value={formData.username}
                        onChange={e =>
                          handleInputChange('username', e.target.value)
                        }
                        isInvalid={!!errors.username}
                        placeholder="Database username"
                        disabled={isSubmitting}
                        className="form-control-compact"
                        autoComplete="off"
                        data-form-type="other"
                        spellCheck={false}
                      />
                      {errors.username && (
                        <div className="invalid-feedback-inline">
                          {errors.username}
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Password */}
                  <div className="form-row-compact form-row-compact-reduced">
                    <label htmlFor="password" className="form-label-inline">
                      Password <span className="text-danger">*</span>
                    </label>
                    <div className="form-input-wrapper">
                      <Form.Control
                        id="password"
                        type="password"
                        value={formData.password}
                        onChange={e =>
                          handleInputChange('password', e.target.value)
                        }
                        isInvalid={!!errors.password}
                        placeholder="Database password"
                        disabled={isSubmitting}
                        className="form-control-compact"
                        autoComplete="new-password"
                        data-form-type="other"
                      />
                      {errors.password && (
                        <div className="invalid-feedback-inline">
                          {errors.password}
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              </>
            )}{' '}
            {/* Security Notice */}
            <div className="security-notice-compact">
              <span className="notice-icon-small">🛡️</span>
              <span className="notice-text-compact">
                All credentials are encrypted using AES-256 encryption and never
                leave your local machine
              </span>
            </div>
          </Form>
        )}
      </Modal.Body>

      <Modal.Footer className="modal-footer-modern">
        {schemaError.show ? (
          // Error state - no footer buttons, actions are in the modal body
          <div className="footer-info-text">
            <span className="text-muted small">
              Please select an action above to continue
            </span>
          </div>
        ) : (
          // Normal state buttons
          <>
            <Button
              variant="outline-secondary"
              onClick={handleClose}
              disabled={isSubmitting || isCheckingSchema}
              className="btn-cancel"
            >
              Cancel
            </Button>
            <Button
              variant="primary"
              onClick={handleSubmit}
              disabled={isSubmitting || isCheckingSchema}
              className="sage-ai-database-create-btn"
            >
              {isSubmitting ? (
                <>
                  <div className="spinner-modern"></div>
                  {editConfig
                    ? 'Updating Connection...'
                    : 'Creating Connection...'}
                </>
              ) : isCheckingSchema ? (
                <>
                  <div className="spinner-modern"></div>
                  Loading Schema...
                </>
              ) : (
                <>
                  <span className="btn-icon">⚡</span>
                  {editConfig ? 'Update Connection' : 'Create Connection'}
                </>
              )}
            </Button>
          </>
        )}
      </Modal.Footer>
    </Modal>
  );
}
